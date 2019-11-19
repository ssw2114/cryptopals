#!/usr/bin/env python3
import base64

def intToByteLength(i):
    length = i.bit_length() // 8
    if i % 8 == 0:
        return length
    return length + 1

def toBase64(hex):
    integer = int(hex, 16)
    result = base64.b64encode(integer.to_bytes(intToByteLength(integer),
        byteorder='big'))
    return result

print(toBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
