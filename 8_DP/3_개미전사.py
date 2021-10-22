
N = int(input())
stock = list(map(int, input().split()))

dp = [0] * N

dp[0] = stock[0]
dp[1] = max(dp[0], stock[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + stock[i])

print(dp[N-1])


"""
4
1 3 1 5

"""