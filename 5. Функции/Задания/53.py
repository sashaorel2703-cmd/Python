def is_palindrome(n):
    s = 0
    t=n
    while t != 0:

        x = t % 10
        t = t // 10
        s = s*10 + x

    return s == n



a=int(input())
b=int(input())
while a < b:
    if is_palindrome(a):
        print(a, end=' ')
    a+=1
