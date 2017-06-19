#!/usr/bin/env python3
"""Show the odd occurence in an array. Codility problem."""


def Solution(A):
    """Return the odd occurence in an array."""
    B = []
    for i in range(0, len(A)):
        B.append(False)
    for j in range(0, len(A)):
        if B[j] is False:
            for k in range(j+1, len(A)):
                if B[k] is False:
                    if A[j] == A[k]:
                        B[j] = True
                        B[k] = True
                        break
    for l in range(0, len(A)):
        if B[l] is False:
            break
    return A[l]


niz = [9, 3, 9, 3, 9, 7, 9]
print(Solution(niz))
