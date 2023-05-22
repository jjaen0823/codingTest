import sys

input = sys.stdin.readline


def print_rank_list(score_list):
    count, rank, rank_list = 1, 1, [0] * N
    before_score = score_list[0][1]
    rank_list[score_list[0][0]] = rank

    for j in range(1, N):
        if before_score == score_list[j][1]:
            count += 1
        else:
            rank += count
            count = 1
        rank_list[score_list[j][0]] = rank

        before_score = score_list[j][1]

    print(*rank_list)


# input
CONTEST_COUNT = 3
N = int(input())

# 각 대회의 점수의 idx, score 딕셔너리
score_list = [list(map(int, input().rstrip().split())) for _ in range(CONTEST_COUNT)]
score_with_idx = [[[idx, score] for idx, score in enumerate(scores)] for scores in score_list]
# 각 대회의 등수 합 idx, score 딕셔너리
score_sum = [[idx, 0] for idx in range(N)]
for i in range(CONTEST_COUNT):
    for j in range(N):
        score_sum[j][1] += score_list[i][j]

# 점수 기준 정렬
for idx in range(CONTEST_COUNT):
    score_with_idx[idx].sort(key=lambda x: x[1], reverse=True)
score_sum.sort(key=lambda x: x[1], reverse=True)

# output
# 각 대회별 등수
for i in range(CONTEST_COUNT):
    print_rank_list(score_with_idx[i])

# 최종 등수
print_rank_list(score_sum)