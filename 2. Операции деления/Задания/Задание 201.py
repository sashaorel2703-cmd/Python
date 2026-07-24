x=int(input())
s=x%60
m=(x%3600)//60
h=x//3600

print(f"{h}:{m}:{s}")