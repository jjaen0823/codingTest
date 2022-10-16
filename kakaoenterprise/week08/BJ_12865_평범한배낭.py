from sys import stdin

input = stdin.readline

N, K = map(int, input().rstrip().split())
V = [0] * (K + 1)
dp = [0] * (K + 1)
for _ in range(N):
    w, v = map(int, input().rstrip().split())
    V[w] = v

for i in range(1, K+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + V[k])

print(dp[K])


"""
4 7
6 13
4 8
3 6
5 12

"""