#!/usr/bin/env python3
"""Find missing integer in an array"""


def solution(A):
    """Find missing integer in array A!"""

    while i < duz:
        if A[i] == tmp:
            tmp = A[i] + 1
            i = 0
        i = i + 1
    return tmp


unos = [1, 3, 6, 4, 1, 2, 7, 8, 9, 1, 2, 5]
print(solution(unos))
