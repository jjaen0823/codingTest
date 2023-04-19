import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
# 배열
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
dp[1][1], dp[1][2], dp[2][1] = arr[0][0], arr[0][1], arr[1][0]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for d in dp:
    print(d)

# 합을 구할 부분의 개수 K
K = int(input())
# K 줄의 x1, y1, x2, y2
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])



"""
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3

"""
