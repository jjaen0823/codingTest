
def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:  # left
        return binary_search(arr, target, start, mid - 1)
    else:  # right
        return binary_search(arr, target, mid + 1, end)


N, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, N - 1)
if not result:
    print(f"{target} 없음")
else:
    print(f"index: {result}")
