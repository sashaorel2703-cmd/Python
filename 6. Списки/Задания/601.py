lst = list(map(int, input().split()))
s = 0
for i in range(1, len(lst) - 1):
    if lst[i + 1] < lst[i] > lst[i - 1]:
        s += 1
print(s, end=" ")
