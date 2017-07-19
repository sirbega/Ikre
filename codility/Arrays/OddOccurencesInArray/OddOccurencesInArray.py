#!/usr/bin/env python3
"""Show the odd occurence in an array. Codility problem."""


def solution(A):
    """Return the odd occurence in an array."""
    A = sorted(A)
    duz = len(A) - 1
    i = 0
    while i < duz:
        if A[i] == A[i + 1]:
            i += 2
        else:
            break
    return A[i]


niz = [9, 3, 9, 3, 9, 7, 9]
print(solution(niz))
