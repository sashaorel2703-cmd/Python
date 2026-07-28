n=int(input())
zero = 0
negative=0
positive=0
p=0
for i in range(1,n+1):
    x=int(input())
    if x == 0:
       zero += 1
    if x < 0:
        negative += 1

    if x > 0:
        positive += x
        p +=1

print(f"Нулей: {zero}\nОтрицательных: {negative}\nСреднее положительных: {positive/p:.2f}")
