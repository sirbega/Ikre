#!/usr/bin/env python3
"""FrogJmp: Count minimal number of jumps from position X to Y."""


def solution(X, Y, D):
    """Calculate minimal number of jumps from position X to Y."""
    if (Y - X) % D == 0:
        return(Y - X) // D
    if (Y - X) % D > 0:
        return(Y - X) // D + 1


print(solution(10, 85, 30))
