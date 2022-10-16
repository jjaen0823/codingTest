from sys import stdin

input = stdin.readline

N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]
dp[1] = p[1]

i = 0
for i in range(1, N+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])

print(dp[i])


"""
5
10 9 8 7 6


반례
7
742 3302 5186 6619 567 5068 8591

"""