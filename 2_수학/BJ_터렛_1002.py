import sys
from math import sqrt

input = sys.stdin.readline

def solution(xyr_list):
    cnt = 0
    x1, y1, r1, x2, y2, r2 = xyr_list

    AB = sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    # 같은 원
    if (AB == 0) and (r1 == r2):
        return -1
    elif (AB == abs(r1 - r2)) or (AB == abs(r1 + r2)):
        return 1
    elif abs(r1 - r2) < AB < (r1 + r2):
        return 2
    else:
        return 0


T = int(input())
xyr_2d_list = [list(map(int, input().split())) for _ in range(T)]

for xyr in xyr_2d_list:
    print(solution(xyr))

"""
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5


2
1
0
"""