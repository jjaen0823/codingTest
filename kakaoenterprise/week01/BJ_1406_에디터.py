import sys
from collections import deque

input = sys.stdin.readline

# cursor 는 left 와 right 를 자르는 기준
left, right = deque(input().rstrip()), deque()
N, M = len(left), int(input())

for _ in range(M):
    cmds = list(map(str, input().rstrip().split()))
    if cmds[0] == 'L' and len(left) > 0:
        right.appendleft(left.pop())
    elif cmds[0] == 'D' and len(right) > 0:
        left.append(right.popleft())
    elif cmds[0] == 'B' and len(left) > 0:
        left.pop()
    elif cmds[0] == 'P':
        left.append(cmds[1])

print("".join(left+right))

"""
### 1
abcd
3
P x
L
P y

### 2
abc
9
L
L
L
L
L
P x
L
B
P y

### 3
dmih
11
B
B
P x
L
B
B
B
P y
D
D
P z

"""