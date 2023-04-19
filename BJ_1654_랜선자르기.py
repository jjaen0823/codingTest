import sys
input = sys.stdin.readline

def number_of_n(val, k_list):
    n = 0
    for k_len in k_list:
        n += k_len // val
    return n

def solution(k, n, k_list):
    ans = 0
    min_n_len, max_n_len = 1, k_list[-1]

    # Binary Search logic
    while min_n_len <= max_n_len:
        mid_n_len = (min_n_len + max_n_len) // 2

        if number_of_n(mid_n_len, k_list) >= n:  # 개수가 크거나 같은 경우 -> 길이 증가
            min_n_len = mid_n_len + 1
            ans = mid_n_len
        else:  # 개수가 적은 경우 -> 길이 감소
            max_n_len = mid_n_len - 1

    return ans


K, N = list(map(int, input().split()))
K_list = sorted([int(input()) for _ in range(K)])

print(solution(K, N, K_list))



"""
랜선자르기
백준 실버 2

문제
N개의 랜선 필요.
K개의 랜선을 이미 갖고 있음. but, 길이는 제각각
-> K개의 랜선을 잘라서 모두 N개의 같은 길이의 랜선으로 만들어야 함 

* 이미 자른 랜선의 나머지 길이들은 이어 붙일 수 없음!
* 항상 기존의 K개의 랜선으로 N개의 랜선을 만들 수 있음!
* 항상 센티미터 단위의 정수 길이 만큼 자를 수 있음!

=> 만들 수 있는 최대 랜선의 길이를 구하시오.


입력
K, N
K1
K2
…

1 <= K <= 10**4
1 <= N <= 10**6
출력
만들 수 있는 최대 랜선의 길이

———————————
일단 가장 짧은 랜선 길이보다 길 수는 없다.
max = 길이가 가장 짧은 랜선
min = 

어떤 알고리즘일까효~?
이분 탐색으로 길이를 찾는게 가장 효율적일 것 같음. 헉 맞다 이분 탐색


4 11
802
743
457
539

"""
