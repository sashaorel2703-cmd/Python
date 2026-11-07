n=input()
x=''
y=0
for i in n :
    if i == 'a' :
        x += 'b'
        y+=1
    elif i == 'b' :
        x+='a'
        y += 1
    elif i == 'A' :
        x+='B'
        y += 1
    elif i == 'B' :
        x+='A'
        y += 1
    else:
        x+=i
print(x,y,sep="\n")
