import sys

input = sys.stdin.readline

T = int(input().rstrip())

if T % 10 != 0:
    print(-1)
else:
    a, T = T // 300, T % 300
    b, T = T // 60, T % 60
    c = T // 10
    print(a, b, c)


