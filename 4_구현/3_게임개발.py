# 북, 동, 남, 서 (U, R, D, L)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


N, M = map(int, input().split())
x, y, direction = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

turn_limit = 0
count = 1  # 처음 위치가 육지기 때문에 이미 하나는 방문한 상태
visited[x][y] = 1

while True:
    # 왼쪽 방향으로 회전
    turn_left()
    # 해당 방향 앞으로 한칸 방문
    nX = x + dx[direction]
    nY = y + dy[direction]
    # 회전 후, 정면에 가보지 않는 육지가 존재하는 경우
    if game_map[nX][nY] == 0 and visited[nX][nY] == 0:
        visited[nX][nY] = 1
        x, y = nX, nY
        count += 1
        turn_limit = 0
        continue
    else:
        turn_limit += 1

    if turn_limit == 4:
        nX = x - dx[direction]
        nY = y - dy[direction]
        if game_map[nX][nY] == 0:  # 육지인 경우 뒤로 이동
            x, y = nX, nY
        else:  # 뒤가 바다인 경우 멈추기
            break
        turn_limit = 0

print(count)




"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

"""

