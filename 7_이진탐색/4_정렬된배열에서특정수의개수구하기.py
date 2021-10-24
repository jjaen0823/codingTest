import sys
from collections import Counter

input = sys.stdin.readline

N, target = map(int, input().split())
count = Counter(list(map(int, input().split())))
print(count[target])

"""
7 2
1 1 2 2 2 2 3

"""

# bisect 라이브러리 활용해서 풀어보리