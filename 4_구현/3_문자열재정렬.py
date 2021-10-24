str_list = list(input())
str_list.sort()
sum_ = 0
str_ = ''
for s in str_list:
    if 65 <= ord(s) <= 90:  # A ~ Z
        str_ += s
        continue
    else:
        sum_ += int(s)

print(str_ + str(sum_))
"""
K1KA5CB7

AJKDLSI412K4JSJ9D

"""