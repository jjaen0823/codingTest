import sys

input = sys.stdin.readline


def binary_search_H(start, end):
    global arr, M

    H = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for l in arr:
            if l > mid:  # 떡이 잘리는 경우
                total += l - mid

        if total < M:  # 떡이 덜 잘린 경우 H 줄여주기
            end = mid - 1
        else:  # 떡이 충분한 경우 H 늘려주기 + 결과 저장
            H = mid
            start = mid + 1

    return H


N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
print(binary_search_H(0, max(arr)))  # H 범위 0 ~ 가장 긴 떡의 길이 (max(arr))

"""
4 6
19 15 10 17

"""
