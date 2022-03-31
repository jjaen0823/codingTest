import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
TP = deque([list(map(int, input().rstrip().split())) for _ in range(N)])
TP.appendleft([0, 0])
dp = [0] * (N+1)

for i in range(1, N+1):
    if TP[i][0] > (N-i+1):  # 남은 일 수보다 상담 일 수가 더 긴 경우는 아예 상담할 수 없음
        continue
    max_t = 0
    for j in range(i, 0, -1):  # i일을 선택 하는 경우 자신 보다 작은 일수 중 상담이 가능한 날 중 max 값 선택
        if (i-j) >= TP[j][0] and dp[j] > max_t:  # 상담 가능한 날 + dp[j]가 max_t보다 클 때
            max_t = dp[j]  # max 값 변경
    dp[i] = max_t + TP[i][1]

# print(dp)
print(max(dp))



"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10


"""