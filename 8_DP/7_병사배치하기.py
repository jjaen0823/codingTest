# 어려웡ㅜ
# 가장 긴 증가하는 부분수열과 유사한 문제!! BJ 11053

N = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()  # 오름차순
dp = [1] * N

# 가장 긴 수열을 만들고 전체 길이에 빼면, 제외한 길이가 나옴
for i in range(1, N):
    for j in range(i):
        if soldiers[i] > soldiers[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))


"""
7
15 11 4 8 5 2 4

"""