max_number=-float('inf')
while (n := int(input())) != 0:
    if n>max_number:
        max_number=n
print(max_number)