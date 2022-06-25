H, M = map(int,input().split()) # split()으로 띄어쓰기 구분

if H == 0 :
    H += 24

T = H * 60 + M - 45

print(T // 60, T % 60)

