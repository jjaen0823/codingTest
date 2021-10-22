N = int(input())

arr = [tuple(map(str, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: int(x[1]))

for student in arr:
    print(student[0], end=' ')


"""
2
홍길동 95
이순신 77

"""