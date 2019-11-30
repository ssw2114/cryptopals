#!/usr/bin/env python3

def encode(s, key):
    keys = list(map(lambda char:ord(char), list(key)))
    tracker = 0
    result = ''
    byteMessage = bytes(s, 'utf-8')
    for b in byteMessage:
        key = keys[tracker]
        encodedByte = b ^ keys[tracker]
        xordHex = hex(encodedByte)[2:]
        result = result + xordHex
        tracker = (tracker + 1) % len(keys)
    return result

message = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'

print(encode(message, 'ICE'))
