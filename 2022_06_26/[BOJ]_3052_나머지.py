num_list = []
div_list = []
count = 0
for i in range(10) :
    num_list.append(int(input()))
    div_list.append(num_list[i] % 42)
div_set = set(div_list) # set은 중복을 제거하고 순서가 없다.
div_result = list(div_set)
print(len(div_result))