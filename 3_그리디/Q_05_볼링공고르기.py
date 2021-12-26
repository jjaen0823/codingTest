import sys

input = sys.stdin.readline

N, M = map(int, input().split())
bolls = list(map(int, input().split()))
cnt = [0] * 10

for boll in bolls:
    cnt[boll] += 1

result = 0
# 1부터 M 까지의 각 무게에 대하여 처리
for i in range(1, M+1):
    N -= cnt[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += cnt[i] * N  # cnt[i]: 무게가 i 인 공 개수 / N: 무게가 i 가 아닌 공 개수

print(result)

"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

"""
