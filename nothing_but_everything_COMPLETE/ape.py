#!/usr/bin/env python

from glob import glob
import os


directory = '1262404985085867488371'

def clarify(number):
    return hex(int(number))[2:].replace('L','').decode('hex')

# print glob(directory)
os.chdir(directory + '/1466921579')
for i in os.listdir('.'):
    try:
        print clarify(i)
        c = open(i).read()
        # print clarify(c)
        open(clarify(i),'w').write(clarify(c))

    except:
        print "FAILED with ", i


# flag: tjctf{n00b_h4x0r_b357_qu17}