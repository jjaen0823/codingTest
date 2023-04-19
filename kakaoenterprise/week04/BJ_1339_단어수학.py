import sys

input = sys.stdin.readline

N = int(input().rstrip())
words = [list(reversed(list(map(str, input().rstrip())))) for _ in range(N)]
word_dict = {chr(i + 65): 0 for i in range(26)}

for word in words:
    for idx, w in enumerate(word):
        word_dict[w] += 10**idx

sum_ = 0
for idx, val in enumerate(sorted(list(word_dict.values()))[-10:]):
    sum_ += idx * val

print(sum_)

"""

2
GCF
ACDEB

"""