y = int(input())
count = 1
count2 = 1
count_max=1
while (n := int(input())) != 0:
    if n > y:
        count += 1
        count2 = 1
    elif n < y :
        count = 1
        count2 += 1
    else:
        count = 1
        count2 = 1
    y = n
    if count2 > count_max:
        count_max = count2
    if count > count_max:
        count_max = count
print(count_max)

