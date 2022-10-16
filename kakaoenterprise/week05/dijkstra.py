from sys import stdin
import heapq

input = stdin.readline

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [start, distances[start]])

    while queue:
        curr_dest, curr_dist = heapq.heappop(queue)

        if distances[curr_dest] < curr_dist:
            continue

        for new_dest, new_dist in graph[curr_dest].items():
            dist = curr_dist + new_dist
            if dist < distances[new_dest]:  # 알고 있는 거리보다 작으면 갱신
                distances[new_dest] = dist
                heapq.heappush(queue, [new_dest, dist])

    return distances


print(dijkstra(graph, 'A'))