lst = list(map(int, input().split()))
x = int(input())
for i in range(len(lst)):
    if lst[i] < x:
        print(i+1, end=" ")
        break
    if i == len(lst)-1:
        print(len(lst)+1, end=" ")



