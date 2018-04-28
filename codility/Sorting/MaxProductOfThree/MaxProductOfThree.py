#!/usr/bin/env python3
"""Solution for the Max Product of Three problem from codility."""


def solution(A):
    B =  sorted(A, reverse = True)
    return max(B[0] * B[1] * B[2], B[0] * B[-1] * B[-2])

unos = [-3, 1, 2, -2, 5, 6]
print(solution(unos))
