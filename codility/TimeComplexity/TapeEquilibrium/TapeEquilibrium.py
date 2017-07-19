#!/usr/bin/env python3
"""Solve the TapeEquilibrium problem from codility."""


def solution(A):
    duz = len(A)
    if duz == 2:
        return abs(A[0] - A[1])
    totalsum = sum(A)
    sumA = A[0]
    sumB = totalsum - sumA
    chk = abs(sumA - sumB)
    for i in range(1, duz - 1):
        if chk == 0:
            break
        sumA = sumA + A[i]
        sumB = sumB - A[i]
        dif = abs(sumA - sumB)
        if dif < chk:
            chk = dif
    return chk


unos = [3, 1, 2, 4, 3]
print(solution(unos))
