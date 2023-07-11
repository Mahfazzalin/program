#!/bin/python3

#Sockets
#my first socket connection buildup.
# nc -nvlp 7777 '7777 is a port number, 
#MAHFAZZALIN SHAWON REZA

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is a port
s.connect((HOST,PORT))
