import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    gold_dp = [temp[i * M:(i + 1) * M] for i in range(N)]

    for j in range(1, M):
        for i in range(1, N):
            # i-1 이 배열 범위를 넘어가는 경우
            if i-1 < 0:
                gold_dp[i][j] += max(gold_dp[i][j-1], gold_dp[i+1][j-1])
            # i+1 이 배열 범위를 넘어가는 경우
            elif i+1 >= N:
                gold_dp[i][j] += max(gold_dp[i-1][j-1], gold_dp[i][j-1])
            else:
                gold_dp[i][j] += max(gold_dp[i - 1][j - 1], gold_dp[i][j - 1], gold_dp[i+1][j-1])

    print(max(list(zip(*gold_dp))[M-1]))


# 2차원 리스트 column 추출
# list(zip(*gold_dp))[col_idx])

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2


"""