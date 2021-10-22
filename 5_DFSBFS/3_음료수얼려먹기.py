from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    need_visit = deque([(x, y)])
    # print(need_visit)
    while need_visit:
        x, y = need_visit.popleft()

        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nX = x + dx[i]
                nY = y + dy[i]
                if 0 <= nX < N and 0 <= nY < M:
                    if not visited[nX][nY] and graph[nX][nY] == 0:
                        need_visit.append((nX, nY))

    return


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]  # 구멍: 0, 칸막이: 1
visited = [[False] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:  # 구멍이 뚫려있는 부분 + 방문하지 않은 부분이어야 함!
            bfs(i, j)
            count += 1


print(count)

"""
15 14 
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00011110000000
11111111110011
11100011111111
11100011111111

"""