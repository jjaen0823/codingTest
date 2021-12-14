import sys

input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for i in range(N)]
dp = [[0]*(i+1) for i in range(N)]

# init
dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(len(triangle[i])):
        if j-1 < 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j >= len(dp[i-1]):
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

print(max(dp[N-1]))


"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

"""