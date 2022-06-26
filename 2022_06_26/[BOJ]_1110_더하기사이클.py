n = int(input())
count = 0 # 사이클 카운트
num_list = []
num_list.append(n)

while True :
    sum_n = n // 10 + n % 10
    if sum_n < 10 :
        new_n = str(n % 10) + str(sum_n)
    else :
        new_n = str(n % 10) + str(sum_n % 10) 
    if num_list[0] == int(new_n) :
        print(count+1)
        break
    else :
        count += 1
        num_list.append(int(new_n))
        n = int(new_n)