from collections import deque

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
tickets = [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]


def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    stack = ['ICN']
    ans = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:  # 길이 끊어진 경우에 해당하는 것이 마지막 공항이다!!
            ans.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    return ans[::-1]


# def solution2(tickets):
#     tree = {}
#     for k, v in tickets:
#         if k not in tree.keys():
#             tree[k] = [v]
#             continue
#         tree[k].append(v)
#     to_ = 'ICN'  # 'ICN' 공항에서 출발
#     visited = []
#
#     for i in range(len(tickets) + 1):
#         if i == len(tickets):
#             visited.append(to_)
#             return visited
#         if tree[to_]:
#             from_ = min(tree[to_])
#             tree[to_].remove(from_)
#             visited.append(to_)  # 방문 순서
#             to_ = from_


print(solution(tickets))