from collections import deque


def solution(n, wires):
    count_set = set()
    networks = {num: set() for num in range(1, n + 1)}

    # networks 초기하
    for v1, v2 in wires:
        networks[v1].add(v2)
        networks[v2].add(v1)

    # wire 자르기
    for v1, v2 in wires:
        v1_count = bfs(networks, v1, v2)  # v1_count v1에 연결된 송전탑 개수
        if v1_count < n:  # network가 2개로 나눠졌다면 n개보다 적어야 함
            count_set.add(abs(n - 2 * v1_count))

    return min(count_set)


def bfs(graph, v1, v2):
    need_visit = deque([v1])
    visited, v_count = set(), 0

    while need_visit:
        v = need_visit.popleft()
        # 아직 방문하지 않은 송전탑인 경우
        if v not in visited:
            # v1 : {v2}, v2: {v1} 은 끊어졌기 때문에 v1->v2 이동 X
            if v == v1:
                for check_v in graph[v]:
                    if check_v != v2: need_visit.append(check_v)
            else:
                need_visit.extend(graph[v])
            v_count += 1
            visited.add(v)

    return v_count


