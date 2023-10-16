from .nostrmq import NostrMQ
from nostr.key import PrivateKey
import json
from nostr.event import Event
from .errors import PublishError


class Producer(NostrMQ):

    def __init__(
        self,
        relays: list,
        private_key: str,
    ):
        super().__init__(relays=relays)
        self._private_key = PrivateKey.from_nsec(private_key)
        self._public_key = self._private_key.public_key

    def send(self, message):
        super().send(message)
        for websocket in self._websockets:
            if websocket is not None:
                response = json.loads(websocket.recv())
                if response[0] != 'OK':
                    raise PublishError(response)

    def produce(self, message):
        event = Event(
            public_key=self._public_key.hex(),
            content=message,
        )
        self._private_key.sign_event(event)
        self.send(event.to_message())
