#!/usr/bin/env python3
"""Find missing integer in an array"""


def solution(A):
    """Find missing integer in array A!"""
    N = len(A) + 1
    B = [False] * N
    for i in A:
        if i > 0 and i < N:
            B[i] = True
    for j in range(1, N):
        if not B[j]:
            break
    return j


unos = [1, 3, 6, 4, 1, 2, 8, 9, 1, 2, 5, 12, 13, 15, -1, -6]
print(solution(unos))
