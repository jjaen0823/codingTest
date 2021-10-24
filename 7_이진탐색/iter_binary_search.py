

def binary_search(target, start, end):
    global array

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


N, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(target, 0, N - 1)
if not result:
    print(f"{target} 없음")
else:
    print(f"index: {result}")


"""
10 7
1 3 5 7 9 11 13 15 17 19

"""