# A를 B번 곱한 수를 C로 나눈 나머지 출력
def dac(a, b):
    # b가 1인 경우에는 곱할 필요가 없기에 그냥 나머지 리턴.
    if b == 1:
        return a % C

    # dac 함수를 통해 a를 (b // 2)번 곱한 나머지를 구함.
    tmp = dac(a, b // 2)

    # b가 짝수인 경우
    if b % 2 == 0:
        return tmp * tmp % C
    # b가 홀수인 경우
    else:
        return tmp * tmp * a % C


A, B, C = map(int, input().split())

print(dac(A, B))
