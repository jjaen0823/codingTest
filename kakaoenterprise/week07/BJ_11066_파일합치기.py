from sys import stdin
from math import log2, ceil

input = stdin.readline


def solution(N, files):
    n = N
    dp = [files if i == 0 else [0]*(N+1) for i in range(ceil(log2(N)+1))]
    ans = 0
    minus = 0
    # print(dp, len(dp))
    for i in range(1, len(dp)):
        before = n
        last_idx = before - 1
        n = ceil(n / 2)
        for j in range(n):
            dp[i][j] = dp[i-1][j*2] + dp[i-1][j*2+1]
        if before % 2 == 0:  # even
            ans += sum(dp[i])
            print("Even", sum(dp[i]))
        elif before % 2 != 0 and n != 1:  # odd
            minus += dp[i-1][last_idx]
            print("Odd", sum(dp[i-1][:last_idx]) ,dp[i-1][last_idx])
            ans += sum(dp[i-1][:last_idx])
        print(ans)

    for d in dp:
        print(d)
    return ans - minus


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    print(solution(N, list(map(int, input().rstrip().split()))+[0]))



"""
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32


"""