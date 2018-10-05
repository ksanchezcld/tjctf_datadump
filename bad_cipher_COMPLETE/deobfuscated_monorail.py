#!/usr/bin/env python3

message = "tjctf{y34hh_m4ybe_1_sh0ulndt_wr1t3_mY_3ncRypT10N_MY5elf}"
key = "G0S$V=}K"
# output = "473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554"


def transpose(s):
    """Transpose the matrix s"""
    # Example:
    # In: ["ABC", "DEF", "GHI"]
    # Out:['ADG', 'BEH', 'CFI']

    return ["".join(y) for y in zip(*s)]

def string_chunks(s, n):
    """Divide the string s into a list of strings of length n"""

    out = []
    while len(s) >= n:
        out.append(s[:n])
        s = s[n:]
    return out

def hexify(c):
    """Convert a character c to a hex byte, padded with 0"""
    # zfill is used here to ensure numbers that fit in 4 bits are
    # padded all the way out

    return hex(ord(c))[2:].zfill(2)

def encode(message,key):
    scrambled = string_chunks(message, len(key))
    scrambled = transpose(scrambled)
    out = []

    for n,k in enumerate(key):
        a = 0
        e = ""
        for c in scrambled[n]:
            a = ord(c)^ord(k)^(a//4)
            e += chr(a)
        out.append(e)

    out = "".join(transpose(out))
    out = "".join(hexify(c) for c in out)
    return out

print(encode(message,key))