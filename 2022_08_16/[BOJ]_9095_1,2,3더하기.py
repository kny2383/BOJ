# DP(Dynamic Programming) 문제
# n > 3 일때, f(n) = f(n-1) + f(n-2) + f(n-3)

def cal(n):
    if n == 1:
        return 1 # 1 -> 1 1개
    elif n == 2: 
        return 2 # 2 -> 1 + 1, 2 2개
    elif n == 3:
        return 4 # 3 -> 1 + 1 + 1, 1 + 2, 2 + 1, 3 4개
    else:
        return cal(n-1) + cal(n-2) + cal(n-3)

for _ in range(int(input())):
    n = int(input())
    print(cal(n))