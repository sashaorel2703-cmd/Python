max_number=-float('inf')
t1=0
t2=0
count=0
while (n := int(input())) != 0:
    count +=1
    if n >max_number:
        t1=count
    if n>=max_number:
        max_number = n
        t2=count


print(t1,t2)
