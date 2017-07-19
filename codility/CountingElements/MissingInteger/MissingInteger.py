#!/usr/bin/env python3
"""Find missing integer in an array"""


def solution(A):
    """Find missing integer in array A!"""
    B = sorted(A)
    N = len(A)
    tmp = 1
    for i in range(0, N):
        if tmp == B[i]:
            tmp += 1
        if tmp < B[i]:
            break
    return tmp


unos = [1, 3, 6, 4, 1, 2, 8, 9, 1, 2, 5, 12, 13, 15, -1, -6, 7]
print(solution(unos))
