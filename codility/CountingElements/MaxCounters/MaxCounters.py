#!/usr/bin/env python3
"""Solution to the MaxCounters problem from Codility."""


def solution(N, A):
    maxi = 0
    B = [0] * N
    duz = len(A)
    for i in range(0, duz):
        if A[i] == N + 1:
            B = [maxi] * N
        else:
            B[A[i] - 1] += 1
            if maxi < B[A[i] - 1]:
                maxi = B[A[i] - 1]
    return B


unos = [3, 4, 4, 6, 1, 4, 4]
print(solution(5, unos))
