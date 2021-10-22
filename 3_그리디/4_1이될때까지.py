
n, k = map(int, input().split())
count = 0

# while n >= k:
#     if n % k == 0:
#         n //= k
#         count += 1
#     else:
#         plus_count = n % k
#         n -= plus_count
#         count += plus_count
#     # print(n)

while n >= k:
    if n % k != 0:
        plus_count = n % k
        n -= plus_count
        count += plus_count
    n //= k
    count += 1

count += n - 1

print(count)

"""
while n >= k:
    # n 이 k 로 나누어 떨어지지 않는다면 n 에서 1씩 뺀다
    while n % k != 0:
        n -= 1
        count += 1
    
    n //= k
    count += 1
    

# 마지막으로 남은 수에 대해 1씩 빼기
while n > 1:
    n -= 1
    count += 1
    
print(count)
"""