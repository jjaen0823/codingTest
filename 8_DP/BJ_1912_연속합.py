import sys

input = sys.stdin.readline

N = int(input())
dp = list(map(int, input().rstrip().split()))

for i in range(1, N):
    dp[i] = max(dp[i-1] + dp[i], dp[i])

print(dp)
print(max(dp))


"""
10
10 -4 3 1 5 6 -35 12 21 -1

답: 33

10
-10 -4 30 1 5 6 -35 12 21 -1

답: 42
"""