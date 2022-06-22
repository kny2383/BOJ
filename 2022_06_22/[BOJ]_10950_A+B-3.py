T = int(input())
add = []
for i in range(0,T) :
    a, b = map(int,input().split())
    add = add + [a,b]
for i in range(0,T) :
    print(add[2*i]+add[2*i+1])
