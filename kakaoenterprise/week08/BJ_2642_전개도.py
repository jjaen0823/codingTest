from collections import deque
from sys import stdin

input = stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = 6
map = [list(map(int, input().rstrip().split())) for _ in range(N)]
opposite = {i: 0 for i in range(1, N+1)}


def dfs(s):
    # init
    need_visit = deque([s])
    visited = [[False] * N for _ in range(N)]
    direction = {i: None for i in range(len(dx))}
    for i in range(len(dx)):
        nX, nY = s[0] + dx[i], s[1] + dy[i]
        if 0 <= nX < N and 0 <= nY < N and map[nX][nY] != 0:  # 처음 위치에서 갈 방향이 있다는 의미
            direction[i] = (nX, nY)  # 처음 위치에서 상 하 좌 우 방향으로 가면 nX, nY 자리라는 의미

    target_queue = deque([])
    target_d = -1
    while need_visit:
        x, y = need_visit.popleft()
        if (x, y) in direction.values():
            target_d = target_queue.popleft()
        visited[x][y] = True

        for i in range(len(dx)):
            nX, nY = x + dx[i], y + dy[i]
            if 0 <= nX < N and 0 <= nY < N and map[nX][nY] != 0 and visited[nX][nY] is False:  # 범위 안에 있고, 숫자가 있는 경우
                if direction[i] == (nX, nY):  # 시작점에서의 방향 기록 -> 같은 방향이 한 번 더 나오는 경우 맞은 편 면!
                    target_queue.append(i)
                    need_visit.append((nX, nY))
                    continue
                if target_d == i:  # target 방향이 한 번 더 나온 경우
                    visited[nX][nY] = True
                    opposite[map[nX][nY]] = map[s[0]][s[1]]
                    opposite[map[s[0]][s[1]]] = map[nX][nY]
                    return
                # 방문하지 않은 다른 방향으로 접히는 경우 계속 탐색
                need_visit.appendleft((nX, nY))
    return


for i in range(N):
    for j in range(N):
        if map[i][j] != 0:
            dfs((i, j))

if 0 in opposite.values():
    print(0)
else:
    print(opposite[1])

"""
0 0 0 0 0 0
0 0 0 0 0 0
0 0 5 0 0 0
0 1 2 3 4 0
0 0 6 0 0 0
0 0 0 0 0 0


0 0 0 0 0 0
0 0 0 0 0 0
0 0 5 0 4 0
0 0 1 2 3 0
0 0 0 0 6 0
0 0 0 0 0 0

"""