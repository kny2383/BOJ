import numpy as np
N, B = map(int,input().split()) # N * N 인 행렬 A, A의 B제곱
A = [] 

for i in range(N):
    array = list(map(int,input().split()))
    A.append(array) # print(A) : [[1,2],[3,4]]

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            cal_matrix = 0
            for i in range(n):
                cal_matrix += U[row][i] * V[i][col]
            Z[row][col] = cal_matrix % 1000 
    return Z

def square(A, B):
    if B == 1: # 행렬 A 자신
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    tmp = square(A, B//2)
    print(B, tmp)
    if B % 2: 
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

result = square(A, B)
for r in result:
    print(*r) # x = [1, 2, 3, 4], *x = 1 2 3 4 
