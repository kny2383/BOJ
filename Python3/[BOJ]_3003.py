#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

p = [0 for i in range(6)]
k = [0 for i in range(6)]
p[0],p[1],p[2],p[3],p[4],p[5]=input().split()

k[0]=1
k[1]=1
k[2]=2
k[3]=2
k[4]=2
k[5]=8

for i in range(6):
    print(int(int(k[i])-int(p[i])))

#답
# cp = [1, 1, 2, 2, 2, 8]
# li = list(map(int, input().split()))
# for i in range(6):
#     print(cp[i]-li[i], end=' ')
