from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().rstrip().split())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]


def bfs(start):  # start = (x, y)
    weight = [[-1] * M for _ in range(N)]
    weight[0][0] = 0
    need_visit = deque([start])

    while need_visit:
        x, y = need_visit.popleft()
        for idx in range(4):
            nX, nY = x + dx[idx], y + dy[idx]
            if 0 <= nX < N and 0 <= nY < M:
                if weight[nX][nY] == -1:
                    num = MAP[nX][nY]
                    if num == 0:
                        need_visit.appendleft((nX, nY))
                    else:  # 1 인 경우 나중에 탐색
                        need_visit.append((nX, nY))
                    weight[nX][nY] = weight[x][y] + num

    print(weight[N - 1][M - 1])


bfs((0, 0))



"""
4 2
0001
1000

6 5
000000
111110
000000
011111
000000
# 0

23 3
00101110111000000110100
01001111101010010001100
11000001010110010110000
# 5

6 5
001011
110100
100110
101000
000010
# 1


"""
