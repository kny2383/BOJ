# 입력
num1, op1, num2, op2, num3 = input().split() # num1, num2, num3은 피연산자, op1, op2는 연산자
# 문자 -> 정수형 변환
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

def cal(a,b,op): # 계산 기능 함수
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == "/": 
        if a * b < 0: # if a or b < 0
            return -1*(abs(a)//abs(b)) # 양수로 바꿔 계산한 결괏값에 음수 취하기
        else:
            return a // b

result1 = cal(cal(num1,num2,op1),num3,op2)
result2 = cal(num1,cal(num2,num3,op2),op1)

print(min(result1,result2)) # 계산 결과가 작은 것
print(max(result1,result2)) # 계산 결과가 큰 것