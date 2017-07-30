#!/usr/bin/env python3
"""Solution for the Distinct problem from codility."""


def solution(A):
    return len(set(A))


unos = [2, 1, 1, 2, 3, 1]
print(solution(unos))
