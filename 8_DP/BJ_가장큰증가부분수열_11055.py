# 가장 긴 증가하는 부분수열과 유사한 문제!! BJ 11053

N = int(input())
A = list(map(int, input().split()))
dp = A[:]  # 값만 복사

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+A[i])  # A[i] 를 더했을 때와 안 더했을 때의 max 값

print(max(dp))


"""
10
1 100 2 50 60 3 5 6 7 8

"""