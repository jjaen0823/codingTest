
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

first = arr[n-1]
second = arr[n-2]
result = 0

if first == second:
    result = m * first
else:
    count = m // (k + 1)
    mod = m % (k + 1)
    result = count * (k * first + second) + mod * first

print(result)

"""
5 8 3
2 4 5 4 6

"""