from itertools import combinations

def is_unique(candidate_keys, combi):
    for key in candidate_keys:
        if set(key).issubset(set(combi)):  # 최소성
            return False
    return True


def solution(relation):
    ROW, COL = len(relation), len(relation[0])

    # 가능한 모든 row 조합
    candidate_combi = []
    for i in range(1, COL + 1):
        candidate_combi.extend(combinations(range(COL), i))

    # 최소 후보키인지
    candidate_keys = []
    for combi in candidate_combi:
        tmp = [tuple([item[key] for key in combi]) for item in relation]

        # 최소성
        if not is_unique(candidate_keys, combi): continue
        # 유일성
        if len(set(tmp)) == ROW: candidate_keys.append(combi)

    return len(candidate_keys)

# 가장 긴 런타임 2.72ms
