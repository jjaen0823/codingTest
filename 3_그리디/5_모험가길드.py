from collections import deque

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
group = deque()
count = 0

for x in arr:
    group.append(x)
    if len(group) == max(group):
        count += 1
        group = deque()

print(count)


"""
5
2 3 1 2 2

"""