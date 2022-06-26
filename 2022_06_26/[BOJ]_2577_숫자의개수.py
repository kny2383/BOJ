a = int(input())
b = int(input())
c = int(input())
result = a*b*c
result_list = list(map(int,str(result))) # 각 자리수를 list로 변환
count = [0] * 10
for i in range(len(result_list)) :
    for j in range(0,10) :
        if result_list[i] == j :
            count[j] += 1     

for j in range(10) :
    print(count[j])

## 더 간단한 풀이
#a = int(input())
#b = int(input())
#c = int(input())

#result = list(str(a * b * c))
#for i in range(10):
#    print(result.count(str(i)))