def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        map = bin(i | j)[2:].zfill(n)
        # a12=a12.rjust(n,'0')
        map = map.replace('1', '#')
        map = map.replace('0', ' ')
        answer.append(map)
    return answer


def solution2(n, arr1, arr2):
    ans = ['' for _ in range(n)]
    map1 = [[] for _ in range(n)]
    map2 = [[] for _ in range(n)]
    for i in range(n):
        map1[i] = list(format(arr1[i], 'b').zfill(n))
        map2[i] = list(format(arr2[i], 'b').zfill(n))

    for i in range(n):
        string = ''
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                string += ' '
            else:
                string += '#'
        ans[i] = string
    return ans