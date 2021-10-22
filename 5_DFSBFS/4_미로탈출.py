from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start):
    need_visit = deque([start])

    while need_visit:
        x, y = need_visit.popleft()

        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nX = x + dx[i]
                nY = y + dy[i]
                if 0 <= nX < N and 0 <= nY < M:
                    if not visited[nX][nY] and graph[nX][nY] == 1:
                        distance[nX][nY] = distance[x][y] + 1
                        need_visit.append((nX, nY))

    return


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]  # 괴물: 0, 길: 1
distance = [[1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
start = (0, 0)

bfs(start)
print(distance[N-1][M-1])


"""
5 6
101010
111111
000001
111111
111111

"""