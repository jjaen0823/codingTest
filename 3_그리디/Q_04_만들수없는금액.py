import sys

input = sys.stdin.readline

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:  # target 보다 coin 이 큰 경우 => target 금액을 만들 수 없음
        break

    target += coin

print(target)


"""
5
3 2 1 1 9

"""