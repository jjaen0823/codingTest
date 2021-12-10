num_lists = [{'one': '1', 'two': '2', 'six': '6'}, {'zero': '0', 'four': '4', 'five': '5', 'nine': '9'},
             {'three': '3', 'seven': '7', 'eight': '8'}]


def solution(s):
    ans = ""
    idx = 0
    while idx < len(s):
        if str.isdigit(s[idx:idx+1]):
            ans += s[idx:idx+1]
            idx += 1
        else:
            for i, nums in enumerate(num_lists):
                n = s[idx:idx + i+3]
                if n in nums:
                    ans += nums[n]
                    idx += (i + 3)

    return ans


num_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}


def solution2(s):
    answer = s
    for k, v in num_dict.items():
        ans = ans.replace(k, v)
    return int(answer)


s = "one4seveneight"
# idx = 0
# ans = ""
# if str.isdigit(s[idx:idx + 1]):
#     ans += s[idx:idx + 1]
#     idx += 1
#     print(ans)
# else:
#     print(s[idx: idx+0+3])
#     print(s[idx: idx+1+3])
#     print(s[idx: idx+2+3])

print(solution(s))
print(solution2(s))
