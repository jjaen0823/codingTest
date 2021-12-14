# 가장 긴 증가하는 부분수열과 유사한 문제!! BJ 11053

N = int(input())
A = list(map(int, input().split()))
A.reverse()  # 오름차순
dp = [1] * N

# 뒤집어서 가장 긴 수열을 만들면 됨
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


"""
6
10 30 10 20 20 10

"""