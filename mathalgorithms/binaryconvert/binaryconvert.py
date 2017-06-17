#!/usr/bin/env python3


def bindivision(num):
    mod = ""
    bi = ""
    while num > 0:
        tmp = num % 2
        mod = str(tmp)
        bi = mod + bi
        num = num // 2
    return bi


afile = open("binary.txt", "w")
inp = int(input('Input decimal number to convert to binary!  '))
afile.write(bindivision(inp))
afile.close()
