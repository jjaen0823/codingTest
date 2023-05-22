import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dp = [[0]*N for _ in range(N)]  # N * N
dp[0] = list(map(int, input().rstrip().split()))
for i in range(N):
    for j, num in enumerate(list(map(int, input().rstrip().split()))):
        dp[i][j] += dp


for _ in range(M):
    _, _, x2, y2 = map(int, input().rstrip().split())
