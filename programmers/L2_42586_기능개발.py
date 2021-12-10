from math import ceil


def solution(progresses, speeds):
    ans = []
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    idx, count = 0, 0

    while idx < len(days):
        max_day = days[idx]
        count = 1
        for inner_i in range(idx+1, len(days)):
            if days[inner_i] <= max_day:
                count += 1
                idx += 1
            else:
                ans.append(count)
                break
        idx += 1
    ans.append(count)

    return ans


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([93, 30, 55], [1, 30, 5]))
