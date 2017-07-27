#!/usr/bin/env python3
"""Solutioin to the PermCheck problem from Codility."""


def solution(A):
    """Check if an array is a permutation."""
    A = sorted(A)
    duz = len(A)
    povrat = 1
    for i in range(0, duz):
        if A[i] != i + 1:
            povrat = 0
            break
    return povrat


unos = [4, 1, 3, 2]
print(solution(unos))
