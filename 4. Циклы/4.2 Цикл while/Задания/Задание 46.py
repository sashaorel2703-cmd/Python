A=int(input())
B=int(input())
while A > B:
    if A%2 == 0 and A>=2*B :
        A /= 2
        print(f":2")
    else:
        A -= 1
        print(f"-1")

