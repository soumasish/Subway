"""Created by sgoswami on 5/2/17 as part of subway"""
import socket


class Listener:
    def __init__(self):
        self._serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self._serversocket.bind(socket.gethostbyname(), 80)
        self._serversocket.listen(5)
