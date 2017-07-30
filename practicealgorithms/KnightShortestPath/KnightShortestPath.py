#!/usr/bin/env python3
"""Finds the shortest path for the chess figure knight."""


def solution(A, B):
    chk = True
    matrix = [[-1 for x in range(B + 5)] for y in range(A + 5)]
    matrix[2][2] = 0
    i = 0
    while chk:
        chk = False
        for xi in range(2, A + 2):
            for yi in range(2, B + 2):
                if matrix[xi][yi] == i:
                    if matrix[xi + 2][yi + 1] == -1:
                        matrix[xi + 2][yi + 1] = i + 1
                        chk = True
                    if matrix[xi + 2][yi - 1] == -1:
                        matrix[xi + 2][yi - 1] = i + 1
                        chk = True
                    if matrix[xi - 2][yi + 1] == -1:
                        matrix[xi - 2][yi + 1] = i + 1
                        chk = True
                    if matrix[xi - 2][yi - 1] == -1:
                        matrix[xi - 2][yi - 1] = i + 1
                        chk = True
                    if matrix[xi + 1][yi + 2] == -1:
                        matrix[xi + 1][yi + 2] = i + 1
                        chk = True
                    if matrix[xi + 1][yi - 2] == -1:
                        matrix[xi + 1][yi - 2] = i + 1
                        chk = True
                    if matrix[xi - 1][yi + 2] == -1:
                        matrix[xi - 1][yi + 2] = i + 1
                        chk = True
                    if matrix[xi - 1][yi - 2] == -1:
                        matrix[xi - 1][yi - 2] = i + 1
                        chk = True
        i += 1
        if i == 100000000:
            return -2
        if not chk:
            return -1
        if not matrix[A + 2][B + 2] == -1:
            return i


print(solution(99, 99))
