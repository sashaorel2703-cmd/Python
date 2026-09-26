n = int(input())
x = list(map(int, input().split()))


def sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


x.sort(key=sum, reverse=True)
print(*x)
