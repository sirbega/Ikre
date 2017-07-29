#!/usr/bin/env python3
"""Solution to the MaxCounters problem from Codility."""


def solution(N, A):
    maxval = 0
    curr = 0
    B = [0] * N
    duz = len(A)
    for i in range(0, duz):
        if A[i] <= N:
            if curr > B[A[i] - 1]:
                B[A[i] - 1] = curr
            B[A[i] - 1] += 1
            if maxval < B[A[i] - 1]:
                maxval = B[A[i] - 1]
        else:
            curr = maxval
    for j in range(0, N):
        if B[j] < curr:
            B[j] = curr
    return B


unos = [3, 4, 4, 6, 1, 4, 4]
print(solution(5, unos))
