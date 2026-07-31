"""
        n = int(input())
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        print(s)
"""


def sum_num(n):
    if n > 0:
        return sum_num(n // 10) + n % 10
    else:
        return 0


print(sum_num(123))
