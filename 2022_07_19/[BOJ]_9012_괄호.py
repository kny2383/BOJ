for _ in range(int(input())):
    vps = input() # 괄호 문자열 vps 입력 받기
    vps_list = list(vps) # list로 변환
    sum = 0
    for i in vps_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')