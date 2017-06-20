#!/usr/bin/env python3
"""Find the missing element in a zero indexed array of integers."""


def solution(A):
    """Find the missing element in the array A."""
    for i in range(1, len(A)+1):
        chk = True
        for j in range(0, len(A)):
            if A[j] == i:
                chk = False
                break
        if chk:
            break
    return i


niz = [2, 3, 1, 5, 6, 7, 10, 9]
print(solution(niz))
