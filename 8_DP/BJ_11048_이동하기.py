import sys

input = sys.stdin.readline

dx = [-1, 0, -1]
dy = [-1, -1, 0]

N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]  # 사탕 미로

for i in range(N):
    for j in range(M):
        max_candy = [0, 0, 0]
        # dp[i][j] += max(dp[x][y-1], dp[x-1][y-1], dp[x-1][y])
        for idx in range(3):
            if 0 <= i + dx[idx] < N and 0 <= j + dy[idx] < M:
                max_candy[idx] = dp[i + dx[idx]][j + dy[idx]]  # 미로 안에 있는 경우만 max 값 넣어줌
        dp[i][j] += max(max_candy)

print(dp[N-1][M-1])


"""
3 4
1 2 3 4
0 0 0 5
9 8 7 6

3 3
1 0 0
0 1 0
0 0 1

4 3
1 2 3
6 5 4
7 8 9
12 11 10

"""