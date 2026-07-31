"""
def to_bin(num):
    while num > 0:
        print(num % 2)
        num //= 2
"""
def to_bin(num):
    if num >0 :
        to_bin(num//2)
        print(num%2,end="")

to_bin(10)