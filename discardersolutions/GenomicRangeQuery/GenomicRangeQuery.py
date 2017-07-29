#!/usr/bin/env python3
"""Solution for the GenomicRangeQuery problem from codility."""


def solution(S, P, Q):
    M = len(P)
    dic = {"A": 1, "C": 2, "G": 3, "T": 4}
    out = [0] * M
    for i in range(0, M):
        chk = 5
        for j in range(P[i], Q[i] + 1):
            if dic[S[j]] < chk:
                chk = dic[S[j]]
                if chk == 1:
                    break
        out[i] = chk
    return out


SS = "TC"
PP = [0, 0, 1]
QQ = [0, 1, 1]
print(solution(SS, PP, QQ))
