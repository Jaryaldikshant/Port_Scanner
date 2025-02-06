#!/usr/bin/python3

import socket
import sys
import threading


usage = "python3 port.py TARGET,START_PORT, END_PORT"

print("-"*70)
print("PORT SCANNER")
print("-"*70)

if(len(sys.argv) != 4):
	print(usage)
	sys.exit()

try:
	target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
	print("Name Resolution error")
	sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])


print("Scanning Target:",target)



def scan_port(port):
	
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		result = s.connect_ex((target,port))
		
		if result == 0:
			print(f"Port {port} is OPEN")
		s.close()
	except Exception as e:
		print(f"Error Scanning Port {port}:{e}")

threads = []

for port in range(start_port,end_port+1):
	
	thread = threading.Thread(target = scan_port, args = (port,))
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()

print("Scanning completed")

