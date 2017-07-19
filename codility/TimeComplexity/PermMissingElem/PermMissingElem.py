#!/usr/bin/env python3
"""Calculate the missing element in a zero indexed array of integers."""


def solution(A):
    """Calculate the missing element in the array A."""
    chk = 0
    for j in range(0, len(A)):
        chk = chk + A[j]
    return (((len(A)+1)*(len(A)+2))/2) - chk


niz = [2, 3, 1, 5, 6, 7, 10, 9, 8]
print(solution(niz))
