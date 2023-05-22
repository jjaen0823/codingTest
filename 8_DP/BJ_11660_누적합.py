import sys

input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
dp = [[0]+list(map(int, input().rstrip().split())) if i != 0 else [0]*(N+1) for i in range(N+1)]
xy_list = [list(map(int, input().rstrip().split())) for _ in range(M)]

# 누적합 table 만들기
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# 누적합 구하기
for x1, y1, x2, y2 in xy_list:
    print(dp[x2][y2] - (dp[x2][y1-1] + dp[x1-1][y2]) + dp[x1-1][y1-1])

"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4



"""