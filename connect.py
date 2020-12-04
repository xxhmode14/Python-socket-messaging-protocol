#!/usr/bin/env python3
import socket
import readline
import os
import threading
import time
ip_addr = "127.0.0.1" # the server public ip address or keep it as is for a local server
port = 8888

datas = []

def Beautify(text : bytes):
    text = repr(text).replace("\\n","\n").replace("\\x1b","\033")
    text = text[1:]
    text = text[1:]
    text = text[:len(text) - 1]
    return text

def recv_data():
    while not sock._closed:
        data = sock.recv(1024)
        data = Beautify(data)
        if data == "SOCKET CLOSED":
            exit(0)
        print(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ip_addr,port))
    t = threading.Thread(target=recv_data)
    t.start()
    def exit_conn():
        sock.sendall(bytes("-$close","utf-8"))
        exit(0)
    try:
        while True:
            i = input("> ")
            if i == "":
                continue
            if i == "clear" or i == "cls":
                os.system("clear")
                continue
            if i.startswith("-$"):
                i = i[2:]
                if i == "close" or i == "exit":
                    exit_conn()
            sock.send(bytes(i,"utf-8"))
            time.sleep(0.5)
    except KeyboardInterrupt:
        exit_conn()

    