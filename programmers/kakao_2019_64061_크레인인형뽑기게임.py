from collections import deque


def solution(board, moves):
    ans = 0
    N = len(board)
    stack = deque()
    for idx, mv in enumerate(moves):  # mv: 1~N
        for h in range(N):
            if board[h][mv-1] != 0:  # 맨 위 인형
                doll = board[h][mv-1]
                board[h][mv-1] = 0
                if stack and stack[-1] == doll:
                    stack.pop()
                    ans += 2
                else:
                    stack.append(doll)
                break
    return ans