n = int(input())
count = 0 # 한수 개수

if n < 100: # 입력값이 한, 두 자리 일 경우
    print(n) # 입력값이 한, 두 자리이면 비교 대상이 없기 때문에 모두 한수임
else:
    for num in range(100,n+1): # 입력값이 세 자리 일 경우
        n_list = list(map(int,str(num))) # 입력값의 각 자리를 리스트로 구성
        if (n_list[1] - n_list[0]) - (n_list[2] - n_list[1]) == 0: # 등차수열일 경우
            count += 1 # 한수 카운트 증가
    print(99+count) # 99(100 이전까지의 한수) + 한수 카운트