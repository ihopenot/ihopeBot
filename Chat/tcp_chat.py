from .chat import BaseChat
import socket

class TcpChat(BaseChat):
    def __init__(self, config) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((config["ip"], config["port"]))

    def chat(self, msg):
        self.client.send(msg.encode('utf-8'))
        reply = self.client.recv(10240).decode('utf-8')
        return reply