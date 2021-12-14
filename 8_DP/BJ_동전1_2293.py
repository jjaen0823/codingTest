import sys

input = sys.stdin.readline


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0] * (K + 1)
dp[0] = 1  # 2 원을 만들 때, 동전 2원을 쓰는 경우가 1가지 인 것을 알려주기 위해 2-2=0

for c in coins:
    for i in range(c, K + 1):
        dp[i] += dp[i-c]

print(dp[K])

"""
3 10
1
2
5

"""