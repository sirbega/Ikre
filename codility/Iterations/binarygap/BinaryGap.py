#!/usr/bin/env python3
"""Return the binary representation of the input integer."""


def solution(N):
    """Return the longest binary gap of the input integer."""
    mod = ""
    bi = ""
    num = N
    while num > 0:
        tmp = num % 2
        mod = str(tmp)
        bi = mod + bi
        num = num // 2
    broj = bi
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
