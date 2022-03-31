import sys
from itertools import combinations

input = sys.stdin.readline


N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_combi = combinations(cards, 3)
sum_cards = [sum(c) for c in cards_combi if sum(c) <= M]

print(max(sum_cards))




"""
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295

"""