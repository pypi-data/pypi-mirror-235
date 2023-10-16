#!/usr/bin/env python
# -*- coding: utf-8 -*-

from websocket import create_connection


class NostrMQ:

    def __init__(self, relays: list):
        self._relays = relays
        self._websockets = [None] * len(relays)

    def connect(self):
        for index, relay in enumerate(self._relays):
            self._websockets[index] = create_connection(relay)

    def send(self, message):
        for websocket in self._websockets:
            if websocket is not None:
                websocket.send(message)

    def close(self):
        for websocket in self._websockets:
            if websocket is not None:
                websocket.close()
