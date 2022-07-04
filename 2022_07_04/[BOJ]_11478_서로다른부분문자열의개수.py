s = input() # 문자열 입력
result = set() # 중복 허용하지 않는 집합 set 사용

for i in range(len(s)):
    for j in range(i,len(s)):
        temp = s[i:j+1] # 연속된 부분 문자열 구하기
        result.add(temp)
print(len(result))