from collections import deque


def dfs(v):
    global graph, visited
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    global graph, visited
    need_visit = deque([start])

    while need_visit:
        v = need_visit.popleft()

        if not visited[v]:
            print(v, end=' ')
            visited[v] = True
            need_visit.extend(graph[v])


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# dfs(1)
bfs(1)