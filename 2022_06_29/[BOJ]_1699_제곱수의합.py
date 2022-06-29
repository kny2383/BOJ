n = int(input())
squared_num = [] # 제곱수의 합을 담는 리스트
for i in range(n+1):
    squared_num.append(i) # i로 초기화

for j in range(1,n+1):
    for k in range(1,j):
        if k * k > j: # squared_num[j - k * k] 에서 k * k > j 이면 음수이기 때문에 break
            break
        if squared_num[j] > squared_num[j - k * k] + 1:  
            squared_num[j] = squared_num[j - k * k] + 1 # ex) j = 4 이고 k = 2 일때 squared_num[4 - 2 * 2] + 1 = 0 + 1 = 1 => squared_num[4] = 1

print(squared_num[n])