global_arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 9, 10, 10, 8]
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 9, 10, 10, 8]


def quick_sort(start, end):
    global global_arr
    if start >= end:  # 원소기 1개인 경우 종료
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot 보다 큰 data 를 찾을 때까지 반복
        while left <= end and global_arr[left] <= global_arr[pivot]:
            left += 1

        # pivot 보다 작은 data 를 찾을 때까지 반복
        while right > start and global_arr[right] >= global_arr[pivot]:
            right -= 1

        if left > right:  # 엇갈린 경우 작은 데이터와 피벗 교체
            global_arr[right], global_arr[pivot] = global_arr[pivot], global_arr[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            global_arr[left], global_arr[right] = global_arr[right], global_arr[left]

        # 분할 이후
        quick_sort(start, right-1)
        quick_sort(right+1, end)


def python_quick_sort(array):
    # global arr
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 후, 리스트 반환
    return python_quick_sort(left_side) + [pivot] + python_quick_sort(right_side)


print(global_arr)
quick_sort(0, len(arr)-1)
print(global_arr)

print(python_quick_sort(arr))