import sys
from collections import deque

input = sys.stdin.readline

parent = {}
rank = {}


# find root node
def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]


def union(v, u):
    root_v = find(v)
    root_u = find(u)

    # union-by-rank
    # 두 트리의 rank 비교
    # 다른 경우
    # rank가 작은 트리를 큰 트리에 붙인다.
    # 같은 경우
    # 한 쪽 트리 rank += 1 을 하고, 다른 쪽 트리를 해당 트리에 붙인다.
    if rank[root_v] > rank[root_u]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        if rank[root_v] == rank[root_u]:
            rank[root_u] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def min_cost(mst):
    ans = 0
    for edge in mst:
        _, _, weight = edge
        ans += weight
    return ans


def solution(n, costs):
    mst = deque()
    vertices = [n_idx for n_idx in range(n)]  # 0 ~ (n-1)까지의 node

    # 1. initialize
    for node in vertices:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    costs.sort(key=lambda x: x[2])  # v, u, weight -> weight 기준 정렬

    # 3. 간선 연결 (cycle X)
    for edge in costs:
        v, u, weight = edge
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)

    return min_cost(mst)