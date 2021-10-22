
X = int(input())
dp = [0] * (X+1)

for i in range(2, X+1):
    # 1 을 빼는 경우 (항상)
    dp[i] = dp[i-1] + 1
    # 2로 나눠지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나눠지는 경우
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 5로 나눠지는 경우
    elif i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)


print(dp[X])