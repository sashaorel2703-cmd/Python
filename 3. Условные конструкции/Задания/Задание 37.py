n = int(input())
p = n % 10
x = n % 100
if p == 1 and x != 11:
    print("гриб")
elif 2 <= p <= 4 and (x < 11 or 14 < x):
    print("гриба")
else:
    print("грибов")
