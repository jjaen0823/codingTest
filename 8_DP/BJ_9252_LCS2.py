import sys

input = sys.stdin.readline

str1, str2 = input().rstrip(), input().rstrip()
N, M = len(str1), len(str2)

# dp 초기화
dp = [[''] * (M+1) for _ in range(N+1)]

# LCS 구하기
for i in range(1, N+1):
    for j in range(1, M+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + str1[i-1]
        else:
            dp[i][j] = dp[i - 1][j] if len(dp[i-1][j]) >= len(dp[i][j-1]) else dp[i][j-1]

print(len(dp[N][M]))
if len(dp[N][M]) != 0:
    print(dp[N][M])

# pypy3로 해야 시간 초과 안남 ㅠㅠ
"""
ACAYKP
CAPCAK

답: 
4
ACAK

A
A

답: 
1
A

ABCDEFG
BCDEFGA

답: 
6
BCDEFG

ABAABA
AA

답: 
2
AA

"""