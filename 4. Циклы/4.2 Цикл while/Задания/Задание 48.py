start_sum=float(input())
target_sum=float(input())
percent=float(input())
percent /=100
percent /=12
n=0
while start_sum <= target_sum :
    start_sum *= 1 + percent
    n +=1
    print(f"{n} - {start_sum:.2f}")
