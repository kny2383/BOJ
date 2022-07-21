## 후위 표기법
# 피연산자를 먼저 표시하고 연산자를 나중에 표시하는 방법

N = int(input()) # 피연산자의 개수
postfix = input() # 후위표기식

num_list = [0] * N # 피연산자값 저장 변수

for i in range(N):
    num_list[i] = int(input())

stack = []

for i in postfix:
    if 'A' <= i <= 'Z':
        # 스택에 정수형 피연산자값 append
        stack.append(num_list[ord(i)-ord('A')]) # ord(): 문자를 인자로 받아서 유니코드 정수로 반환하는 함수
    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '*':
            stack.append(num1 * num2)
        elif i == '/':
            stack.append(num1 / num2)

print('%.2f' %stack[0])