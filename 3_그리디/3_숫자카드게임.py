
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# sorted_arr = sorted(arr, key=lambda x: min(x))
arr.sort(key=lambda x: min(x))

print(min(arr[n-1]))

"""
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4

"""