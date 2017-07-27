#!/usr/bin/env python3
"""Solutioin to the FrogRiverOne problem from Codility."""


def solution(X, A):
    B = [False] * X
    duz = len(A)
    chk = -1
    for i in range(0, duz):
        B[A[i] - 1] = True
        if all(B):
            chk = i
            break
    return chk


unos = [1, 3, 1, 4, 3, 5, 4, 2]
print(solution(5, unos))
