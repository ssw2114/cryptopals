#!/usr/bin/env python3


def getXor(buff1, buff2):
    int1 = int(buff1, 16)
    int2 = int(buff2, 16)
    print(int1 ^ 1)
    return hex(int1 ^ int2)

print(getXor(b'1c0111001f010100061a024b53535009181c',
    b'686974207468652062756c6c277320657965'))
