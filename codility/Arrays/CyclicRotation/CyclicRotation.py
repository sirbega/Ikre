#!/usr/bin/env python3
"""Rotate an array by a given gap."""


def solution(A, K):
    """Rotate array A by given gap K."""
    duz = len(A)
    if duz == 0:
        return A
    K = K % duz
    B = A[-K:] + A[:-K]
    return B


niz = [3, 8, 9, 7, 6]
print(solution(niz, 3))
