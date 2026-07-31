def max_num(n, max_digit=0):
    if n == 0:
        return max_digit
    return max_num(n//10,max(max_digit,n%10))


print(max_num(123589))

"""n=int(input())
max_number = 0
while n > 0:
    if n % 10 > max_number:
        max_number = n %10
    n //= 10
print(max_number)"""
"""
def max_num(n, max_digit):
if n > 0:
    if (n % 10) > max_digit:
        max_digit = n % 10
    max_num(n // 10, max_digit)
return n
"""