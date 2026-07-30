def perfect_number(number):
    s = 0
    for i in range(1, number):
        if number % i == 0:
            s += i

    return s == number


n = int(input())
s = 0
count = 0
while count < n:
    s += 1
    if perfect_number(s):
        count +=1
        print(s, end=' ')


