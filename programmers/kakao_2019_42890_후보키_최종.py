from itertools import combinations


def is_unique(candidate_keys, combi):
    for key in candidate_keys:
        if key.issubset(combi):  # 최소성
            return False
    return True


def solution(relation):
    ROW, COL = len(relation), len(relation[0])
    transform_relation = list(map(list, zip(*relation)))

    # 최소 후보키인지
    candidate_keys = []
    for i in range(1, COL + 1):
        for combi in combinations(range(COL), i):
            # 최소성
            if not is_unique(candidate_keys, combi): 
                continue

            # 유일성
            row_data_list = [row_data for idx, row_data in enumerate(transform_relation) if idx in combi]
            row_data_combi = list(zip(*row_data_list))
            if len(set(row_data_combi)) == ROW:
                candidate_keys.append(set(combi))

    return len(candidate_keys)

# 가장 긴 런타임 0.83ms
