# 모든 원소의 값이 0 보다 크거나 같다고 가정
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count_sort = [0] * (max(arr) + 1)

for num in arr:
    count_sort[num] += 1

for i, count  in enumerate(count_sort):
    for _ in range(count):
        print(f"{i}", end=" ")


