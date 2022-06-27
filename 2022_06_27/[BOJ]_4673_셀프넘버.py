def d(n) :
    n = n + sum(map(int,str(n))) # n + n의 각 자리 수의 합
    return n

nonSelfNum = set() # 셀프 넘버가 아닌 수들이 들어갈 집합

for i in range(1,10001) :
    nonSelfNum.add(d(i))

for j in range(1,10001) :
    if j not in nonSelfNum:
        print(j)