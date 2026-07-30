def sum_divisors(number):
    s = 0
    for i in range(1, number):
        if number % i == 0:
            s += i
    return s


n = int(input())
for i in range(1, n + 1):
    b = sum_divisors(i)
    if i == sum_divisors(b) and b > i and b <= n:
        print(f"({i},{b})", end=" ")
