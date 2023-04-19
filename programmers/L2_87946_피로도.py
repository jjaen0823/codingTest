from itertools import permutations


def solution(k, dungeons):
    max_dungeon_count = 0
    dungeons_order_list = list(permutations(dungeons, len(dungeons)))

    for dungeons_order in dungeons_order_list:
        curr_k, dungeon_count = k, 0
        for need_degree, consume_degree in dungeons_order:
            if curr_k >= need_degree:
                curr_k -= consume_degree
                dungeon_count += 1
        # dungeon_count 값 비교
        if dungeon_count > max_dungeon_count:
            max_dungeon_count = dungeon_count

    return max_dungeon_count


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
# for idx in range(7, 1, -1):2