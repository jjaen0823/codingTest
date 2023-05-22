from sys import stdin

input = stdin.readline

N, K = map(int, input().rstrip().split())
bags = [list(map(int, input().rstrip().split())) if i != 0 else [0, 0] for i in range(N + 1)]
dp = [[0]*(K+1) for _ in range(N+1)]  # dp[n][k] => N번 째 물건까지 살펴보았을 때, 무게가 K인 배낭의 최대 가치

for i in range(1, N+1):  # 물건
    w, v = bags[i]
    for j in range(1, K + 1):  # 무게
        if j - w < 0:  # 물건을 담을 수 없음
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

# print("   ", end='')
# for idx in range(K+1): print(idx, end='  ')
# print()
# for idx, li in enumerate(dp):
#     print(idx, li)
print(dp[N][K])


"""
https://velog.io/@yoopark/baekjoon-12865

4 7
6 13
4 8
3 6
5 12

답: 14

5 7
2 4
4 3
1 1
8 9
1 10

답: 17
"""