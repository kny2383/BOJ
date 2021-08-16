# 처음 내 코드
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())

# print((a**2+b**2+c**2+d**2+e**2)%10)

#정답
res = 0
for n in list(map(int, input().split())):
    res += n**2
print(res%10)