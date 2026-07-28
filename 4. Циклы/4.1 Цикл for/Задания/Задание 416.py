n = int(input())
"""
count=0
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
        count += 1
        if count == n:
            break
    if count == n:
        break
"""
i = 1
count = 0
for _ in range(n):
    print(i, end=" ")
    count += 1
    if count == i:
        count = 0
        i += 1
