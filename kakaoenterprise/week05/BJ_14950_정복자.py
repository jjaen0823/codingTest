from sys import stdin

input = stdin.readline

N, M, t = map(int, input().rstrip().split())

edges = []
for _ in range(M):
    src, dest, cost = map(int, input().rstrip().split())
    edges.append((src, dest, cost))

edges.sort(key=lambda x: x[2])
parent = list(range(N + 1))
# print(edges, parent)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    # 부모가 자기 자신인 경우 (x == parent[x])
    return parent[x]


def union(s, d):
    s = find(s)
    d = find(d)
    # 부모 노드 업데이트 (작은 노드 번호로)
    if s < d:
        parent[d] = s
    else:
        parent[s] = d


# kruskal
total_cost = 0
for s, d, c in edges:
    if find(s) != find(d):
        union(s, d)
        total_cost += c

print(total_cost + t * (N - 2) * (N - 1) // 2)

# https://techblog-history-younghunjo1.tistory.com/262
