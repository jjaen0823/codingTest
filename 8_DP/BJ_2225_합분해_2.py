from sys import stdin

input = stdin.readline

N, K = map(int, input().rstrip().split())
DIV = 10 ** 9


def solution(K, N):
    # init
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    for i in range(1, K+1):
        dp[i][0] = 1
    for j in range(1, N+1):
        dp[1][j] = 1

    # dp logic
    for i in range(2, K+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    return dp[-1][-1]


print(solution(K, N) % DIV)


# 참고: https://didu-story.tistory.com/241
"""
20 2

21

6 4

84

"""