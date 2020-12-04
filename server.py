#!/usr/bin/env python3

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import os
import threading

def print_info(message):
        message = str(message)
        return f"\033[32;1m[+] {message}\033[37;0m\n"

def print_debug(message):
    message = str(message)
    return f"\033[34;1m[!] {message}\033[37;0m\n"

def print_error(message):
    message = str(message)
    return f"\033[31;1m[-] {message}\033[37;0m\n"


def Beautify(text : bytes):
    text = repr(text).replace("\\n","\n")
    text = text[1:]
    text = text[1:]
    text = text[:len(text) - 1]
    return text

def from_print(addr,message):
    message = str(message)
    addr = str(addr)
    return f"\033[32;1m[{addr}]: \033[34m{message}\033[37;0m\n"

def Joind_message(addr):
    addr = str(addr)
    return f"\033[32;1m[{addr}] \033[35m Joind the server!\033[37;0m\n"

def encode_data(data : str):
    return bytes(data,"utf-8")

class sock_server():
    def __init__(self):
        self.HOST = "0.0.0.0"
        self.PORT = 8888
        self.sessions_num = 0
        self.all_connections = []
        self.connected_addresses = []
        self.no_no_commands = []
    def start(self):
        os.system("clear")
        print(print_info(f"Starting on {self.HOST}:{self.PORT}"))
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.bind((self.HOST,self.PORT))
            try:
                while True:
                    sock.listen()
                    conn, addr = sock.accept()
                    print(print_info(f"New connection from {addr}"))
                    t = threading.Thread(target=self.connect,args=(conn,addr))
                    t.start()
                    self.sessions_num += 1
                    print(print_debug(f"Connected to session {self.sessions_num}"))
                    for connection in self.all_connections:
                        connection.send(encode_data(Joind_message(f"{addr[0]}:{addr[1]}")))
                    self.all_connections.append(conn)
                    self.connected_addresses.append(addr)

            except KeyboardInterrupt:
                self.server_close(sock,"KEYBOARD INTERRUPT FROM SERVER")

    def connect(self,conn,addr):
        try:
            while True:
                data = conn.recv(1024)
                data = repr(data)
                data = data[1:]
                data = data[1:]
                data = data[:len(data) - 1]
                if data.split(" ")[0] == "-$close" or data.split(" ")[0] == "-$exit":
                    self.exit(conn,addr,"SOCKET CLOSE REQUEST\n")
                    break
                conn.send(encode_data(from_print("You",data)))
                for connection in self.all_connections:
                    if connection != conn:
                        connection.send(encode_data(from_print(f"{addr[0]}:{addr[1]}",data)))
                print(from_print(f"{addr[0]}:{addr[1]}",data))
        except Exception as e:
            print(print_error(f"an exception ouccourred on the connect function:\n{e}"))
                
    def exit(self,conn,addr,exit_Message):
        try:
            print(print_info(f"address {addr} disconnected from the server"))
            conn.send(bytes(f"{exit_Message}","utf-8"))
            conn.send(bytes("SOCKET CLOSED\n",'utf-8'))
            conn.detach()
            conn.close()
            self.all_connections.remove(conn)
            self.connected_addresses.remove(addr)
            self.sessions_num -= 1
        except Exception as e:
            print(print_error(f"an exception ouccourred on the exit function:\n{e}"))

        
    def server_close(self,sock,exit_Message):
        print(print_error(f"closing the server for {exit_Message}"))
        sock.detach()
        sock.close()
        exit(0)


if __name__ == "__main__":
    sock_server().start()
