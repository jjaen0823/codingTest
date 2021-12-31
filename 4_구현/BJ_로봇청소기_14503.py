import sys

input = sys.stdin.readline

# 0 1 2 3
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


N, M = map(int, input().split())

r, c, d = map(int, input().split())

rooms = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# rooms[r][c] 방문 처리
visited[r][c] = True
cnt = 1

while 1:
    flag = 0

    # 4 가지 방향 확인
    for _ in range(4):
        # 방향 번경 후 작업 시작
        d = (d+3)%4
        nR = r + dx[d]
        nC = c + dy[d]
        if 0 <= nR < N and 0 <= nC < M and rooms[nR][nC] == 0:
            if visited[nR][nC] is False:
                visited[nR][nC] = True
                cnt += 1
                r, c = nR, nC
                # 청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break

    if flag == 0:  # 4 방향 모두 청소 완료
        nR = r-dx[d]
        nC = c-dy[d]
        if rooms[nR][nC] == 1:  # 벽인 경우
            print(cnt)
            break
        else:
            r, c = nR, nC



"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1


11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

"""

# # 북 동 남 서 기준 왼쪽 방향
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# 
# # 북 동 남 서 기준 후진 방향
# bx = [1, 0, -1, 0]
# by = [0, -1, 0, 1]


"""
    idx = 0
    # 1. 현재 위치 청소
    visited[r][c] = True
    cnt += 1

    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸 탐색
    while True:  # 0, 1, 2, 3
        nR = r + dx[d]
        nC = c + dy[d]
        if 0 <= nR < N and 0 <= nC < M:  # 인덱스가 배열 안에 있어야 하고
            # a. 왼쪽 방향 아직 청소 안 했으면, 그 방향으로 회전한 후 전진 -> 1 번 진행 (break)
            if rooms[nR][nC] != 1:  # 벽 아니고,
                if visited[nR][nC] is False:  # 청소 안 되어 있는 경우, 방향 회전 + 한 칸 전진
                    d = (d + 3) % 4  # 방향 변경
                    r, c = nR, nC  # 한 칸 전진
                    break  # 1 부터 다시 진행
                else:  # 청소가 되어 있는 경우, 방향 회전만 실시
                    # idx==3 인 경우는 네 방향 모두 청소를 하지 못 한 경우
                    if idx == 3:
                        bR = r + bx[d]
                        bC = c + by[d]
                        if 0 <= bR < N and 0 <= bC < M:
                            # 뒤가 벽이 아닌 경우
                            if rooms[bR][bC] != 1:
                                # 방향 유지, 후진 후 2번으로 돌아감
                                idx = 0
                                r, c = bR, bC
                                continue
                            # 뒤가 벽인 경우
                            else:
                                print(cnt)
                                sys.exit();
                                # end = True
                                # break
                    else:
                        d = (d + 3) % 4  # 방향 변경
                        idx += 1
                        continue

        else:  # 왼쪽이 벽인 경우
            bR = r + bx[d]
            bC = c + by[d]
            if 0 <= bR < N and 0 <= bC < M:
                # 뒤가 벽이 아닌 경우
                if rooms[bR][bC] != 1:
                    # 방향 유지, 후진 후 2번으로 돌아감
                    idx = 0
                    r, c = bR, bC
                    continue
                # 뒤가 벽인 경우
                else:
                    print("후진 불가", direction[d])
                    print(cnt)
                    sys.exit()

        # 배열 바깥
"""
