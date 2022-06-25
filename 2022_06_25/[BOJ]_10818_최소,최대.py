N = int(input())
num = list(map(int,input().split()))

def solving_max_num(num,N) :
    max_num = num[0]
    for i in range(0,N) :
        if max_num < num[i] :
            max_num = num[i]
    return max_num 

def solving_min_num(num,N) :
    min_num = num[0]
    for i in range(0,N) :
        if min_num > num[i] :
            min_num = num[i]
    return min_num 

print(solving_min_num(num,N),solving_max_num(num,N))