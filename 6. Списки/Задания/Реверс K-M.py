n=int(input())
lst = list(map(int, input().split()))
k,m = map(int,input().split())
lst[k-1:m]=lst[k-1:m][::-1]
print(*lst)