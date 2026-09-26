lst = list(map(int, input().split()))
max_index =0
min_index =0
for i in range(len(lst)):

    if lst[i] >lst[max_index]:
        max_index = i
    if lst[i] < lst[min_index]:
        min_index = i

lst[min_index],lst[max_index]=lst[max_index],lst[min_index]
print(*lst)