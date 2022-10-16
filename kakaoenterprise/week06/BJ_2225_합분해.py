from sys import stdin
import operator as op
from functools import reduce

input = stdin.readline

N, K = map(int, input().rstrip().split())
DIV = 10**9


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


print(nCr(K+N-1, N) % DIV)


"""
20 2

6 4

"""