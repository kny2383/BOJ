a, b = map(int,input().split()) # 숫자 입력 받기
a_list = list(map(int,str(a))) # 첫 번째로 입력 받은 숫자 쪼개서 리스트에 넣기
b_list = list(map(int,str(b))) # 두 번째로 입력 받은 숫자 쪼개서 리스트에 넣기
print(sum(a_list)*sum(b_list)) # 결국엔 두 숫자의 합을 곱하면 된다