n = input().split()
y = ""
for i in n:
    if len(i)>len(y):
        y = i
print(y,len(y),sep='\n')
print(n:=max(n,key=len),len(n),sep='\n')