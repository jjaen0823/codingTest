import sys
from collections import deque

# input = sys.stdin.readline


def bfs(n, k):
    need_visit = deque([n])

    while need_visit:
        x = need_visit.popleft()
        if k == x:
            break
        for nX in (x-1, x+1, x*2):
            if 0 <= nX <= LIMIT and not dist[nX]:  # if 문 순서 중요!!!!!!
                dist[nX] = dist[x] + 1
                need_visit.append(nX)

    return dist[x]


N, K = map(int, input().split())
LIMIT = 10**5
dist = [0] * (LIMIT+1)
print(bfs(N, K))



