## 유클리드 호제법 사용
a, b = map(int,input().split()) # 두 수 입력 받기
def gcd(a, b): # 최대공약수 함수
    while b > 0 :
        a, b = b, a % b
    return a

def lcm(a, b) : # 최소공배수 함수
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

# 파이썬 math 모듈 속에 최대공약수와 최소공배수를 구하는 함수가 내장되어 있음
# import math
#a, b = map(int, input().split())
#print(math.gcd(a, b))
#print(math.lcm(a, b))