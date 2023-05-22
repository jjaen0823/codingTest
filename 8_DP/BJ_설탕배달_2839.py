import sys

input = sys.stdin.readline

N = int(input())
INF = 50001

dp = [INF] * (N+1)
for i in range(1, N+1):
    if i % 3 == 0: dp[i] = i // 3
    if i % 5 == 0: dp[i] = i // 5

    if i > 5:
        dp[i] = min(dp[i], dp[i-3] + 1, dp[i-5] + 1)

if dp[N] == INF:
    print(-1)
else:
    print(dp[N])

"""
18
답: 4

4
답: -1

6
답: 2

"""