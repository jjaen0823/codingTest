import sys

input = sys.stdin.readline

# 고속거듭제공 a^b % m
# e.g. 2^10 = 1 * 2^2 * 2^8
# e.g. 2^11 = (1 * 2) * 2^2 * 2^8
def power(a, b, m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result


MOD = 1000000007
K, P, N = map(int, input().rstrip().split())

print(K*power(P, N, MOD)%MOD)