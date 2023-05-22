import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

# 길이
order = max(dp)
print(order)

# 수열
ans = [0] * order
for idx in range(N-1, -1, -1):
    if dp[idx] == order:
        ans[order - 1] = A[idx]
        order -= 1

print(*ans)


# ans = [0] * max_len
# last_idx, ans[max_len-1] = max_len_idx, A[max_len_idx]
# for idx in range(max_len_idx, -1, -1):
#     if dp[last_idx] == 1: break
#     if dp[idx] == (dp[last_idx] - 1):
#         ans[dp[idx]-1] = A[idx]
#         last_idx = idx
#
# print(*ans)

"""
6
10 20 10 30 20 50

답:
4
10 20 30 50

"""



