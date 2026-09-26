lst = list(map(int, input().split()))
x=float('inf')
for i in range(len(lst)):
    if lst[i] > 0 and lst[i]<x:
        x = lst[i]
print(x, end=" ")
