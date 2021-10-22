N = int(input())
arr = [int(input()) for _ in range(N)]
arr = sorted(arr, reverse=True)

for num in arr:
    print(num, end=' ')
