from sys import stdin

input = stdin.readline

V, S, _ = map(int, input().rstrip().split())

edges = []
for _ in range(S):
    src, dest, cost = map(int, input().rstrip().split())
    edges.append((src, dest, cost))

edges.sort(key=lambda x: x[2])
parent = list(range(V + 1))

print(edges, parent)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(s, d):
    s = find(s)
    d = find(d)

    if s < d:
        parent[d] = s
    else:
        parent[s] = d


total_cost = 0
mst = []
for s, d, c in edges:
    if find(s) != find(d):
        union(s, d)
        mst.append((s, d, c))
        total_cost += c

print(mst)
print(total_cost)
