#!/usr/bin/env python3
"""Solution to the CountDiv problem from Codility."""


def solution(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K)) // K


print(solution(6, 11, 2))
