n,s = map(int,input().split())
a = list(map(int,input().split())) # 동생의 위치
dif = list(set(abs(a[i]-s) for i in range(n)))
d = min(dif)

def gcd(x,y): # 유클리드 호제법
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

for i in range(len(dif)):
    d = gcd(dif[i], d)

print(d)