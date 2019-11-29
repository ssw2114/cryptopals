#!/usr/bin/env python3

#function that takes a hex buffer and an int, xors the int against 
#each byte of the buffer and returns the result
def getXor(hexStr, i):
    bytesFromHexStr = bytes.fromhex(hexStr)
    xorHexStr = ''
    for b in bytesFromHexStr:
        #xor it with i
        xordByte = b ^ i
        #convert result to hex string
        xordHex = hex(xordByte)[2:]
        if len(xordHex) == 1:
            xordHex = '0' + xordHex
        #concatenate w xorHexStr
        xorHexStr = xorHexStr + xordHex
    bytesObj = bytes.fromhex(xorHexStr)
    result = bytesObj.decode('ascii')
    return result

#function that scores string based on character frequency
def getScore(s):
    score = 0
    frequencies = 'etaoinshrdlucmfwypvbgkjqxz'
    scores = {}
    counter = 26
    for i in range(len(frequencies)):
        scores[frequencies[i]] = counter
        counter = counter - 1
    for j in range(len(s)):
        if s[j] in scores:
            score += scores[s[j]]
    return score

def decode(s):
    result = ''
    highScore = 0
    for i in range(128):
        decoded = getXor(s, i)
        score = getScore(decoded)
        if score > highScore:
            highScore = score
            result = decoded 
    return result

print(decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
