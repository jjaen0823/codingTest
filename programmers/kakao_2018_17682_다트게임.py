import re


def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


def solution2(dartResult):
    game_idx, idx = 0, 0
    game = [0, 0, 0, 0]
    print(game)

    while idx < len(dartResult) or game_idx < 3:
        print(game_idx, idx)
        # check num
        if dartResult[idx].isdigit():
            game_idx += 1
            # check 10
            if dartResult[idx:idx + 2] == '10':
                game[game_idx] = 10
                print(game[game_idx])
                idx += 2
            else:
                game[game_idx] = int(dartResult[idx])
                print(game[game_idx])
                idx += 1

        # check SDT
        elif dartResult[idx].isalpha():
            std = dartResult[idx]
            if std == 'D':
                game[game_idx] = game[game_idx] ** 2
            elif std == 'T':
                game[game_idx] = game[game_idx] ** 3
            else:  # 'S'
                pass
            idx += 1

        # check reward
        # elif not dartResult[idx].isalnum():
        else:
            if idx < len(dartResult):
                if dartResult[idx] == '*':
                    if game_idx != 0:
                        game[game_idx - 1] = game[game_idx - 1] * 2
                    game[game_idx] = game[game_idx] * 2

                elif dartResult[idx] == '#':
                    game[game_idx] = game[game_idx] * (-1)
                idx += 1
            else:
                break

    return sum(game)