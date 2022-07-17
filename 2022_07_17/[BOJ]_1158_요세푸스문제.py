N, K = map(int,input().split())
arr = [i for i in range(1,N+1)] # 처음 원
ans = [] # 새로 만든 원
index = 0
for _ in range(N):
    index += (K - 1) # 제거할 인덱스
    if index >= len(arr): 
        index %= len(arr)
    ans.append(str(arr[index]))
    arr.pop(index)

print("<",', '.join(ans),">", sep="")