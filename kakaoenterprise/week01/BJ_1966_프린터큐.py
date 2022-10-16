import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    p_queue = deque([(i, p) for i, p in enumerate(map(int, input().split()))])
    order = 1

    while True:
        first = p_queue[0]
        if any(first[1] < q[1] for q in p_queue):
            p_queue.rotate(-1)
        else:
            p_queue.popleft()
            if first[0] == M:
                print(order)
                break
            order += 1
