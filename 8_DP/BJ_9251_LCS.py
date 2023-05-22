from sys import stdin

input = stdin.readline

str1, str2 = input().rstrip(), input().rstrip()
N, M = len(str1), len(str2)

# dp 초기화
dp = [[0] * (M+1) for _ in range(N+1)]

# LCS 구하기
for i in range(1, N+1):
    for j in range(1, M+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])
"""
ACAYKP
CAPCAK

답: 4

A
A

답: 1

ABCDEFG
BCDEFGA

답: 6

ABAABA
AA

답: 2

"""