"""Created by sgoswami on 5/2/17 as part of subway"""
import socket


class Client:
    def __init__(self):
        self._clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host):
        self._clientsocket.connect(host, 80)
