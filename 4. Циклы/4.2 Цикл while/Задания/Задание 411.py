max_number = -float('inf')
x = 0
while (n := int(input())) != 0:
    if n > max_number:
        max_number = n
        x = 0
    if n == max_number:
        x += 1
print(x)
