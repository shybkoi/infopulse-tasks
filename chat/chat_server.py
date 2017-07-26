# -*- coding: utf-8 -*-

__author__ = "Shybkoi"

# простейший чат
# архитектура такая: Сервер, Клиенты
# Клиенты могут отослать сообщение конкретному другому клиенту или всем
# протокол сообщений Клиент - Сервер:
#1. name: Vasya - означает, что клиент хочет залогинится под ником Vasya
#2. list: - список залогиненых Клиентов
#3. broadcast: Hello - отправить всем сообщение Hello
#4. Pеtya: Hi - адресное послание кллиенту Petya

# протокол сообщений - Сервер - Клиент:
#1. list: Vasya\nPetya\n - список пользователей
#2. Kolya:Hi - присылает Васе адресата от которго пришло сообщение Hi


import socket
import threading


class ClientHandler(threading.Thread):
    def __init__(self, sock, clients):
        super().__init__()
        self.sock = sock
        self.clients = clients

    def run(self):
        while True:
            mess = self.sock.recv(1024).decode()
            array_mess = mess.split(":")
            if array_mess[0] == "name":

                check = self.clients.get(array_mess[1], False)
                if self.sock in self.clients.values():
                    output = "You have already registered!"
                    self.sock.send(output.encode())
                    continue
                if check:
                    output = "This login is busy!"
                    self.sock.send(output.encode())
                    continue
                self.clients[array_mess[1]] = self.sock
            elif array_mess[0] == "list":
                output = ""
                for name in self.clients.keys():
                    output += name + "\n"
                self.sock.send(output.encode())
            elif array_mess[0] == "broadcast":
                sender = ""
                for key, value in self.clients.items():
                    if value == self.sock:
                        sender = key
                        break
                for socket in self.clients.values():
                    socket.send(("%s : %s" % (sender, array_mess[1])).encode())
            elif array_mess[0] == "logout":
                for key, value in self.clients.items():
                    if value == self.sock:
                        del self.clients[key]
                        self.sock.close()
                        raise SystemExit
            else:
                sender = ""
                for key, value in self.clients.items():
                    if value == self.sock:
                        sender = key
                        break
                if sender == "":
                    self.sock.send("You have no registered yet!".encode())
                    continue
                receiver_sock = self.clients[array_mess[0]]
                receiver_sock.send(("%s : %s" % (sender, array_mess[1])).encode())


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 4444))
    sock.listen(5)
    clients = {}
    while True:
        client_sock, client_addr = sock.accept()
        client_handler = ClientHandler(client_sock, clients)
        client_handler.start()


if __name__ == "__main__":
    main()