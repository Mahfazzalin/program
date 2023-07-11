#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#add a pretty banner
print("""MAHFZZALIN SHAWON REZA """) 
print("_"* 50)
print("Scaning targer: "+ target)
print("Time started: "+ str(datetime.now()))
print("_"* 50)

try:
	for port in range(50,88):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\n Exiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not connect to server.")
	sys.exit()
	
