# print(chr(97), ord('a'))  # a, 97

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

position = input()
x = int(position[1])
y = ord(position[0]) - 96

count = 0

for i in range(len(dx)):
    nX = x + dx[i]
    nY = y + dy[i]

    if 1 <= nX <= 8 and 1 <= nY <= 8:
        count += 1

print(count)