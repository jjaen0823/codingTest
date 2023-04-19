import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input().rstrip())
a_len, A = int(input().rstrip()), list(map(int, input().rstrip().split()))
b_len, B = int(input().rstrip()), list(map(int, input().rstrip().split()))

cnt = 0
dict_A = defaultdict(int)  # key: sum, value: count

for i in range(a_len):
    for j in range(i, a_len):
        dict_A[sum(A[i:j+1])] += 1

for i in range(b_len):
    for j in range(i, b_len):
        cnt += dict_A[T - sum(B[i:j+1])]

print(cnt)


"""
5
4
1 3 1 2
3
1 3 2

"""