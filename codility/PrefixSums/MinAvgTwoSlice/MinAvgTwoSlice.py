#!/usr/bin/env python3
"""Solution for the MinAvgTwoSlice problem from codility."""


def solution(A):
    duz = len(A) - 2
    chk = (A[0] + A[1]) * 3
    ind = 0
    for i in range(0, duz):
        if (A[i] + A[i + 1]) * 3 < chk:
            chk = (A[i] + A[i + 1]) * 3
            ind = i
        if (A[i] + A[i + 1] + A[i + 2]) * 2 < chk:
            chk = (A[i] + A[i + 1] + A[i + 2]) * 2
            ind = i
    if (A[duz] + A[duz + 1]) * 3 < chk:
        ind = duz
    return ind


unos = [4, 2, 2, 5, 1, 5, 8]
print(solution(unos))
