import sys
from itertools import combinations, product

input = sys.stdin.readline

VOWELS = ["a", "e", "i", "o", "u"]

L, C = map(int, input().split())
v, c = 1, L - 1

data = list(map(str, input().split()))
vs = [d for d in data if d in VOWELS]
cs = list(set(data) - set(vs))
ans = []

while v <= len(vs) and c >= 2:
    res = list(product(list(map(''.join, combinations(vs, v))), list(map(''.join, combinations(cs, c)))))
    ans.extend([''.join(sorted(r[0] + r[1])) for r in res])
    v += 1
    c -= 1

for d in sorted(ans):
    print(d)

"""
4 6
a t c i s w

"""