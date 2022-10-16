from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# init
R, C = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(R)]
distance = [[0] * C for _ in range(R)]
need_visit = deque()
beaver = tuple()  # 비버 위치 x, y


def bfs():
    while need_visit:
        x, y = need_visit.popleft()
        # 고슴도치가 비버 굴 위치에 도달한 경우
        if graph[beaver[0]][beaver[1]] == 'S':
            return distance[beaver[0]][beaver[1]]

        for idx in range(4):
            nX, nY = x + dx[idx], y + dy[idx]
            if 0 <= nX < R and 0 <= nY < C:
                # 물
                if graph[x][y] == '*' and (graph[nX][nY] == '.' or graph[nX][nY] == 'S'):
                    graph[nX][nY] = '*'
                    need_visit.append((nX, nY))
                # 고슴도치
                elif graph[x][y] == 's' and (graph[nX][nY] == '.' or graph[nX][nY] == 'D'):
                    graph[nX][nY] = 'S'
                    distance[nX][nY] = distance[x][y] + 1
                    need_visit.append((nX, nY))

    return "KAKTUS"


# 위치
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':  # 큐에 고슴도치 위치를 넣어줌
            need_visit.appendleft((i, j))
        elif graph[i][j] == 'D':  # 비버 위치 저장
            beaver = (i, j)

for i in range(R):
    for j in range(C):
        if graph[i][j] == "*":  # 물 위치
            need_visit.append((i, j))

print(bfs())

"""
3 3
D.*
...
.S.

"""
