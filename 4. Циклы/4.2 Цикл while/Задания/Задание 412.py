max_number=-float('inf')
x=-float('inf')
while (n := int(input())) != 0:
    if n>max_number:
        x = max_number
        max_number = n
    elif n>x:
        x=n

print(x)

