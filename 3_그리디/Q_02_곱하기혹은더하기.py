
num_list = list(map(int, input()))
ans = 0

if len(num_list) == 1:
    ans = num_list[0]
else:
    if (num_list[0] == 0 or num_list[0] == 1) or (num_list[1] == 0 or num_list[1] == 1):
        ans += num_list[0] + num_list[1]
    else:
        ans += num_list[0] * num_list[1]

    for idx in range(2, len(num_list)):
        if num_list[idx] == 0 or num_list[idx] == 1:
            ans += num_list[idx]
        else:
            ans *= num_list[idx]

print(ans)