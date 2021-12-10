
string = input()
prev = string[0]
if prev == "0":
    cnt_0, cnt_1 = 1, 0
else:
    cnt_0, cnt_1 = 0, 1

for idx in range(1, len(string)):
    curr = string[idx]
    if prev == curr:
        prev = curr
    else:
        if curr == "0":
            cnt_0 += 1
        else:
            cnt_1 += 1
        prev = curr

print(min(cnt_0, cnt_1))

"""
0001100
1

000110011
2

0101000111
3

"""