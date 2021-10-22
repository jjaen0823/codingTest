N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()  # 오름차순
b = list(map(int, input().split()))
b.sort(reverse=True)  # 내림차순

i, j = 0, 0

for _ in range(K):
    if a[i] < b[j]:
        a[i], b[j] = b[j], a[i]
        i += 1
        j += 1
    else:
        break

print(sum(a))


"""
5 3
1 2 5 4 3
5 5 6 6 5

"""