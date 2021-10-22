
n = int(input())
direct = list(map(str, input().split()))
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direct_types = ["L", "R", "U", "D"]

for d in direct:
    i = direct_types.index(d)
    nX = x + dx[i]
    nY = y + dy[i]

    if 1 <= nX <= n and 1 <= nY <= n:
        x, y = nX, nY

print(x, y)


"""
5
R R R U D D

"""