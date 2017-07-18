#!/usr/bin/env python3
"""Return the binary representation of the input integer."""


def bindivision(num):
    """Return the binary representation of input integer."""
    mod = ""
    bi = ""
    while num > 0:
        tmp = num % 2
        mod = str(tmp)
        bi = mod + bi
        num = num // 2
    return bi


def solution(N):
    """Return the longest binary gap of the input integer."""
    broj = bindivision(N)
    print(broj)
    duz = len(broj)
    tmp = 0
    gap = 0
    for i in range(0, duz):
        for j in range(i, duz):
            if broj[j] == "0":
                tmp = tmp + 1
            if broj[j] == "1":
                break
        if j < duz:
            if broj[j] == "1":
                if tmp > gap:
                    gap = tmp
        tmp = 0
    return gap


N = int(input("Give me a positive integer! "))
print(solution(N))
