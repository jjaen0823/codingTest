import sys

input = sys.stdin.readline


N = int(input().rstrip())
part_list = set(map(int, input().rstrip().split()))
M = int(input().rstrip())
req_list = list(map(int, input().rstrip().split()))

for part_num in req_list:
    if part_num in part_list:
        print("yes", end=" ")
    else:
        print("no", end=" ")


"""
5
8 3 7 9 2
3
5 7 9

"""