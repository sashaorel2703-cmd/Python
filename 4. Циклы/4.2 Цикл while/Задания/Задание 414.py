y=-float('inf')
count=1
result=1
while (n := int(input())) != 0:
    if n == y:
        count+=1
    elif n!=y and count>result:
        result = count
        count = 1
    y=n
print(max(count,result))
