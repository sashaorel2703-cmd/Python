n=input()
s=set()
for c in n:
    if c.isdigit():
        s.add(c)
s = list(s)
s=sorted(s)
if len(s) == 0:
    print("NO")
else:
    print(*s, sep="")