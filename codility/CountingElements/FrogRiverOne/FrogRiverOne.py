#!/usr/bin/env python3
"""Solutioin to the FrogRiverOne problem from Codility."""


def solution(X, A):
    B = [False] * X
    duz = len(A) + 1
    chk = -1
    count = X
    for i in range(0, duz):
        if count > 0:
            if not B[A[i] - 1]:
                B[A[i] - 1] = True
                count -= 1
        else:
            chk = i - 1
            break
    return chk


unos = [1, 3, 1, 4, 3, 5, 4, 2]
print(solution(5, unos))
