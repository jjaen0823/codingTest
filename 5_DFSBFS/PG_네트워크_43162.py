import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    need_visit = deque([start])
    global tree, visited
    count = 0

    while need_visit:
        node = need_visit.popleft()

        if node not in visited:
            count += 1
            need_visit.extend(tree[node])
            visited.append(node)

    return count


N = int(input())
T = int(input())
tree = {num: [] for num in range(1, N+1)}  # tree 초기화
visited = [False] * (N+1)  # index 1 ~ T 만 사용할 것임


for _ in range(T):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)

tree = sorted(tree.items(), key=lambda x: x[1][0])
# tree = dict(sorted(tree.items(), key=lambda x: x[1]))
print(tree)

# print(bfs(1)-1)


"""
7
6
1 5
5 2
5 6
4 7
1 2
2 3


"""
