n,x = map(int,input().split())
a = [] * n
a = list(map(int,input().split()))
k = []
for i in range(n) :
    if a[i] < x :
        k.append(a[i])
for i in range(len(k)) :
    print(k[i],end=" ")
