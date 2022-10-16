from sys import stdin

input = stdin.readline


def solution(row, col, arr):
    # init
    dp = [[0]*col for _ in range(row)]
    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]

    for j in range(1, col):
        for i in range(row):
            dp[i][j] = max(dp[(i+1) % 2][j-1] + arr[i][j], dp[i][j-1])

    return max(map(max, dp))


ROW = 2
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    arr = [list(map(int, input().rstrip().split())) for _ in range(ROW)]
    print(solution(ROW, N, arr))


"""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

"""

"""
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]


def ADD(A, B):
    return [i + j for i, j in zip(A, B)]


def solution(a, b):
    return list(map(ADD, a, b))


solution(a, b)"""
