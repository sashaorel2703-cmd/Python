k = int(input())
m = int(input())
n = int(input())
if n<=k:
    print(2*m)
else:
    c=2*n
    if c%k==0:
        r=(c//k)
        print(r * m)
    else:
        r=(c//k+1)
        print(r*m)


