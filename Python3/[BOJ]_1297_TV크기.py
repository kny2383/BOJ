import math
k=list(map(int,input().split()))
n=float(math.sqrt(int(k[0]**2)/(k[1]**2+k[2]**2)))
print(int(k[1]*n),int(k[2]*n))

