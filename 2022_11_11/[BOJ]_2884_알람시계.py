H, M = map(int, input().split())

if H == 0:
    H = 24

T = H * 60 + M -45

result_H = T//60
result_M = T%60
if result_H >= 24:
    result_H -= 24

print(result_H, result_M)