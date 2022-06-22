n = int(input())

for i in range(n) :
    for j in range(i+1) :
        print("*",end="")
    print("")

## format 간단 코드
#for i in range(n) :
#    print('{:<5}'.format("*"*(i+1)))