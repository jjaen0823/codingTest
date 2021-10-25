from math import comb

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # num = list(combinations([i for i in range(M)], N))
    # M! // (M-N)! * N!
    print(comb(M, N))



"""
3
2 2
1 5
13 29

"""