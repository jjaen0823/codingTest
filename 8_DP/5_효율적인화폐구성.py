import sys

input = sys.stdin.readline


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
INF = 10001
dp = [INF] * (K + 1)
dp[0] = 0
for c in coins:
    dp[c] = 1

for c in coins:
    for i in range(c+1, K + 1):
        dp[i] = min(dp[i], dp[i-c] + 1)

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])


"""
3 15
1
5
12

"""