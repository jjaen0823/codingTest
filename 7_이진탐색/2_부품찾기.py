import sys

input = sys.stdin.readline


def binary_search(target, start, end):
    global part_list
    while start <= end:
        mid = (start + end) // 2

        if part_list[mid] == target:
            return "yes"
        elif part_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return "no"


N = int(input().rstrip())
part_list = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
req_list = list(map(int, input().rstrip().split()))

for part_num in req_list:
    print(binary_search(part_num, 0, N-1), end=" ")


"""
5
8 3 7 9 2
3
5 7 9

"""