import json
from uuid import uuid4
from threading import Thread
from nostr.event import Event
from nostr.key import PublicKey
from .nostrmq import NostrMQ
from .errors import SignatureError
from .utils import CircularDict
from websocket._exceptions import WebSocketTimeoutException


class Consumer(NostrMQ):

    def __init__(
        self,
        relays: list,
        public_key: str,
        cache_size: int = 100,
    ):
        super().__init__(relays=relays)
        self._public_key = PublicKey.from_npub(public_key)
        self._shall_stop = False
        self._cache = CircularDict(cache_size)
        self._consumer_threads = []

    def _disable_timeout(self):
        for websocket in self._websockets:
            websocket.settimeout(None)

    def _enable_timeout(self):
        for websocket in self._websockets:
            websocket.settimeout(.1)

    def consume_target(self, callback):
        while not self._shall_stop:
            for websocket in self._websockets:
                if websocket is not None:
                    try:
                        response = json.loads(websocket.recv())
                    except WebSocketTimeoutException:
                        continue

                    if response[0] == 'EVENT':
                        event = Event(
                            public_key=response[2]['pubkey'],
                            content=response[2]['content'],
                            created_at=response[2]['created_at'],
                            kind=response[2]['kind'],
                            tags=response[2]['tags'],
                            id=response[2]['id'],
                            signature=response[2]['sig'],
                        )
                        if not event.verify():
                            raise SignatureError()
                        if event.id not in self._cache:
                            self._cache[event.id] = event
                            message = {
                                'content': event.content,
                                'timestamp': event.created_at,
                            }
                            callback(message)

    def consume(
        self,
        callback,
        start_timestamp=None,
        stop_timestamp=None,
    ):
        # TODO: create new websocket connections for each subscription
        if len(self._consumer_threads) > 0:
            raise NotImplementedError(
                'Only one subscription per consumer is supported at the moment.'  # noqa: E501
            )

        filter = {'authors': [self._public_key.hex()]}

        if start_timestamp is not None:
            filter['since'] = start_timestamp

        if stop_timestamp is not None:
            filter['until'] = stop_timestamp

        request = ['REQ', str(uuid4()), filter]

        self._disable_timeout()
        self.send(json.dumps(request))
        self._enable_timeout()

        thread = Thread(
            target=self.consume_target,
            args=(callback, ),
            daemon=True,
        )
        thread.start()
        self._consumer_threads.append(thread)

    def join(self):
        for thread in self._consumer_threads:
            thread.join()

    def stop(self):
        self._shall_stop = True
        self.join()
