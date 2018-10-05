#!/usr/bin/env python 

from pwn import *

a = [
p32(0x74636a74),
p32(0x756a7b66),
p32(0x635f3735),
p32(0x5f6c6c34),
p32(0x725f336d),
p32(0x72337633),
p32(0x365f3335),
p32(0x665f6430),
p32(0x5f6d3072),
p32(0x5f77306e),
p32(0x7d6e30)

]

print "".join(a)