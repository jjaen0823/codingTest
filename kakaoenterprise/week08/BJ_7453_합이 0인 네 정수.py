from sys import stdin
from itertools import product

input = stdin.readline

n = int(input())
A, B, C, D = [0]*n, [0]*n, [0]*n, [0]*n
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().rstrip().split())


def solution():
    AB = dict()

    cnt = 0
    for a in A:
        for b in B:
            AB[a+b] = AB.get(a+b, 0) + 1

    for c in C:
        for d in D:
            cnt += AB.get(-(c+d), 0)

    return cnt


print(solution())


def fail_solution():
    ALL = [A, B, C, D]

    cnt = 0
    ans = list(product(*ALL))
    for nums in ans:
        if sum(nums) == 0:
            cnt += 1

    return cnt


print(fail_solution())

'''
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45

'''