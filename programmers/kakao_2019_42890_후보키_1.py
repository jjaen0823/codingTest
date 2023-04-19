from itertools import combinations


def check_not_least_candidate_key(candidate_col_combi, candidate_keys):
    for key in candidate_keys:
        if set(candidate_col_combi).issuperset(key):
            return True
    return False


def check_candidate_key(transform_relation, candidate_col_combi):
    row_data_list = [row_data for idx, row_data in enumerate(transform_relation) if idx in candidate_col_combi]
    row_data_combi = list(zip(*row_data_list))

    return len(row_data_combi) == len(set(row_data_combi))


def solution(relation):
    # 90도 회전 => list(map(list, zip(*arr[::-1])))
    # 행렬 변환 => list(zip(*arr))
    transform_relation = list(map(list, zip(*relation)))
    COLUMN = len(relation[0])
    candidate_keys = []

    for i in range(1, COLUMN + 1):
        for candidate_col_combi in combinations(list(range(0, COLUMN)), i):
            # 이미 최소 후보키가 아니므로
            if check_not_least_candidate_key(candidate_col_combi, candidate_keys) is True:
                continue

            # 후보키 체크
            if check_candidate_key(transform_relation, candidate_col_combi):
                candidate_keys.append(set(candidate_col_combi))

    return len(candidate_keys)

# 가장 긴 런타임 1.50ms
