n = int(input())
num_list = list(map(int,input().split()))
M = max(num_list)
for i in range(n) :
    num_list[i] = num_list[i] / M * 100 
print(sum(num_list) / n)