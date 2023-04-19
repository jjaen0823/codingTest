from sys import stdin

input = stdin.readline

N = int(input())
powers = sorted([list(map(int, input().rstrip().split())) for _ in range(N)])
B = 1
dp = [1] * N
# print(powers)

for i in range(N):
    for j in range(i):
        if powers[i][B] > powers[j][B]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))



"""
# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%802565%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%A0%84%EA%B9%83%EC%A4%84-DP

8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

"""