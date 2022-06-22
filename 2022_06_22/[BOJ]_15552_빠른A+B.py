import sys

T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

## input() 대신 sys.stdin.readline() 사용하는 이유
## 한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는
## input()으로 입력 받는다면 시간초과가 발생할 수 있다.