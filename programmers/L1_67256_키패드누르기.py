mid = [2, 5, 8, 0]

keypads =[[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ["*", 0, "#"]]


def solution(numbers, hand):
    ans = ""
    l_i, l_j = 3, 0
    r_i, r_j = 3, 2
    for num in numbers:
        if num in [1, 4, 7]:
            ans += "L"
            l_i, l_j = num // 3, 0
        elif num in [3, 6, 9]:
            ans += "R"
            r_i, r_j = (num // 3)-1, 2
        else: # 2, 5, 8, 0
            i, j = mid.index(num), 1
            dist_l = abs(l_i - i) + abs(l_j - j)
            dist_r = abs(r_i - i) + abs(r_j - j)
            if dist_l < dist_r:
                ans += "L"
                l_i, l_j = i, j
            elif dist_l > dist_r:
                ans += "R"
                r_i, r_j = i, j
            else:  # ==
                if hand == 'left':
                    ans += "L"
                    l_i, l_j = i, j
                else:
                    ans += "R"
                    r_i, r_j = i, j
    return ans

