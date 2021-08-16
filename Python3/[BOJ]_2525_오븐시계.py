a,b=map(int,input().split())
c= int(input())
k= (b+c)//60
if ((b+c)>=60):
    b = (b+c)-60*k
    a +=k    
elif ((b+c)<60):
    b +=c
if (a>=24):
    a -=24
if (b==60):
    b = 0
print(a,b)

#좋은 풀이
# H, M = map(int, input().split())
# timer = int(input()) 

# H += timer // 60
# M += timer % 60

# if M >= 60:
#     H += 1
#     M -= 60
# if H >= 24:
#     H -= 24

# print(H,M)