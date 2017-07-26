# -*- coding: utf-8 -*-

__author__ = "Shybkoi"


import socket
import threading
import select # позволяет сделать socket асинхронным, чтобы send и recv не блокировали сокет


class ReadThread(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            answer = self.sock.recv(1024).decode()
            print(answer)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 4444))
    select.select([sock], [sock], [])
    read_thread = ReadThread(sock)
    read_thread.start()
    while True:
        message = input()
        sock.send(message.encode())

if __name__ == "__main__":
    main()
