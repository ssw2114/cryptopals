#!/usr/bin/env python3
import challenge_3

f = open('challenge_4_text.txt')

highScore = 0
result = ''

for line in f:
    decoded = challenge_3.decode(str.strip(line))
    score = challenge_3.getScore(decoded)
    if score > highScore:
        highScore = score
        result = decoded

print(result)


