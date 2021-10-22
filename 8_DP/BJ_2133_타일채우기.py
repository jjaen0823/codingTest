
N = int(input())
dp = [0] * (30+1)

dp[2] = 3
dp[4] = 11  # 9+2

for i in range(3, N+1):
    dp[i] = (dp[i-2] * 3 + dp[i-4] * 2)

print(dp[N])
