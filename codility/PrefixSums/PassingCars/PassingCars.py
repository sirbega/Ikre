#!/usr/bin/env python3
"""Solution to the PassingCars problem from Codility."""


def solution(A):
    pair = 0
    zero = 0
    duz = len(A)
    for i in range(0, duz):
        if pair < 1000000000:
            if A[i] == 0:
                zero += 1
            else:
                pair = pair + zero
        else:
            return -1
    return pair


unos = [0, 1, 0, 1, 1]
print(solution(unos))
