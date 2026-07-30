
from math import sqrt


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


n = int(input())
num = 0
count=0
while count < n:
    num += 1
    if is_prime(num):
        count +=1
        print(num,end=" ")


