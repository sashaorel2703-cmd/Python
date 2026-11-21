from menuinst.api import remove

alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
y=""
n = input()
"""for i in n :
    if i.upper() in alp:
        y+=i.upper()"""

n=''.join(c.upper() for c in n if c.upper() in alp)

a = ""
b = ""

for i in alp:
    x = n.count(i)
    a += i * (x // 2)
    if x % 2 == 1:
        b += i
  
if len(b) <= 1:
    print(a[::-1] + b + a)
else:
    print("no")