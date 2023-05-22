import sys

input = sys.stdin.readline

HEIGHT = 100
limit_speed, test_speed = [], []

# input
N, M = map(int, input().rstrip().split())
for idx in range(N):
    length, speed = map(int, input().rstrip().split())
    limit_speed += [speed]*length

for idx in range(M):
    length, speed = map(int, input().rstrip().split())
    test_speed += [speed]*length

# 차이가 가장 많이 나는 속도 값 정렬
diff_speed = sorted([test_speed[i]-limit_speed[i] for i in range(HEIGHT)], reverse=True)

# output
print(max(diff_speed[0],0))
