#!/usr/bin/env python3
"""Solution to the FrogRiverOne problem from Codility."""


def solution(X, A):
    B = [False] * X
    duz = len(A)
    count = X
    for i in range(0, duz):
        if not B[A[i] - 1]:
            B[A[i] - 1] = True
            count -= 1
            if count == 0:
                return i
    return -1


unos = [1, 3, 1, 4, 3, 5, 4, 2]
print(solution(5, unos))
