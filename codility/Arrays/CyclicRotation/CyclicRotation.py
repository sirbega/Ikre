#!/usr/bin/env python3
"""Rotate an array by a given gap."""


def Solution(A, K):
    """Rotate array A by given gap K."""
    B = []
    duz = len(A)
    for i in range(0, duz):
        B.append(0)
    print(B)
    print(A)
    print(duz)
    for j in range(0, duz):
        if j + K >= duz:
            B[j + K - duz] = A[j]
        if j + K < duz:
            B[j + K] = A[j]
    return B


niz = [3, 8, 9, 7, 6]
print(Solution(niz, 3))
