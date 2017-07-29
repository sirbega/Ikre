#!/usr/bin/env python3
"""Solution for the GenomicRangeQuery problem from codility."""


def solution(S, P, Q):
    M = len(P)
    N = len(S)
    out = [0] * M
    mapA = [0] * (N + 1)
    mapC = [0] * (N + 1)
    mapG = [0] * (N + 1)
    mapT = [0] * (N + 1)
    for i in range(0, N):
        mapA[i + 1] = mapA[i]
        mapC[i + 1] = mapC[i]
        mapG[i + 1] = mapG[i]
        mapT[i + 1] = mapT[i]
        if S[i] == 'A':
            mapA[i + 1] += 1
        if S[i] == 'C':
            mapC[i + 1] += 1
        if S[i] == 'G':
            mapG[i + 1] += 1
        if S[i] == 'T':
            mapT[i + 1] += 1
    for j in range(0, M):
        if mapA[Q[j] + 1] - mapA[P[j]] > 0:
            out[j] = 1
        elif mapC[Q[j] + 1] - mapC[P[j]] > 0:
            out[j] = 2
        elif mapG[Q[j] + 1] - mapG[P[j]] > 0:
            out[j] = 3
        elif mapT[Q[j] + 1] - mapT[P[j]] > 0:
            out[j] = 4
    return out


SS = "CAGCCTA"
PP = [2, 5, 0]
QQ = [4, 5, 6]
print(solution(SS, PP, QQ))
