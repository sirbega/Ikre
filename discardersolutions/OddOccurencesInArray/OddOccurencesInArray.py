#!/usr/bin/env python3
"""Show the odd occurence in an array. Codility problem."""


def solution(A):
    """Return the odd occurence in an array."""
    duz = len(A)
    B = [False] * duz
    for j in range(0, duz):
        if B[j] is False:
            for k in range(j + 1, duz):
                if B[k] is False:
                    if A[j] == A[k]:
                        B[j] = True
                        B[k] = True
                        break
    for l in range(0, duz):
        if B[l] is False:
            break
    return A[l]


niz = [9, 3, 9, 3, 9, 7, 9]
print(solution(niz))
