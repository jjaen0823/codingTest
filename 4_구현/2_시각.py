N = int(input())
count = 0

for h in range(0, N+1):
    if h == 3 or h == 13 or h == 23:
        count += 3600
        continue
    for m in range(0, 60):
        for s in range(0, 60):
            if "3" in str(h) + str(m) + str(s):
                count += 1

print(count)

count = 0

for h in range(0, N+1):
    if h == 3 or h == 13 or h == 23:
        count += 3600
    else:
        count += 1575

print(count)