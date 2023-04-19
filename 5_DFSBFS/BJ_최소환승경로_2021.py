import sys
from collections import deque

input = sys.stdin.readline

def solution(src, dest):
    need_visit = deque([(st, 0) for st in station_graph[src-1]])
    visited = {src}
    transfer_count = []

    while need_visit:
        station: int
        station, count = need_visit.popleft()
        # 목적지
        if station == dest:
            transfer_count.append(count)
        # 목적지 X
        if station not in visited:
            # 환승역 check
            visited.add(station)
            need_visit.extend([(st, count+1) if (count_station[st-1] >= 2) else (st, count) for st in station_graph[station-1]])
        else: continue

    print(transfer_count)
    if len(transfer_count) != 0:
        return min(transfer_count)
    return -1


N, L = map(int, input().split())
# {역 번호: [이동 가능한 역 리스트]} 초기화
station_graph = [[] for _ in range(N)]
count_station = [0 for _ in range(N)]

for _ in range(L):
    line = list(map(int, input().split()))
    for idx in range(len(line)-1):
        curr, nxt = line[idx], line[idx + 1]
        if nxt != -1:
            station_graph[curr-1].append(nxt)
            station_graph[nxt - 1].append(curr)
        count_station[curr-1] += 1

# src, dest
S, D = map(int, input().split())

print(solution(S, D))


"""
10 3
1 2 3 4 5 -1
9 7 10 -1
7 6 3 8 -1
1 10


2
"""