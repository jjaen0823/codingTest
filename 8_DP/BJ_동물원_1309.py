import sys

input = sys.stdin.readline

MOD = 9901
N = int(input().rstrip())

dp = [[0]*2 for _ in range(N)]
dp[0][0], dp[0][1] = 2, 1

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] * 2) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD

print(sum(dp[N-1]) % MOD)



"""
4

답: 41

"""