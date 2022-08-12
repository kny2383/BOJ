pw = input()
pw_list = list(pw) # 문자열 pw를 리스트로 변환

for i in range(len(pw_list)):
    if 'a' <= pw_list[i] <= 'm':
        pw_ascii = ord(pw_list[i]) + 13
        pw_list[i] = chr(pw_ascii)
    elif 'n' <= pw_list[i] <= 'z':
        pw_ascii = ord(pw_list[i]) - 13
        pw_list[i] = chr(pw_ascii)
    elif 'A' <= pw_list[i] <= 'M':
        pw_ascii = ord(pw_list[i]) + 13
        pw_list[i] = chr(pw_ascii)
    elif 'N' <= pw_list[i] <= 'Z':
        pw_ascii = ord(pw_list[i]) - 13
        pw_list[i] = chr(pw_ascii)
        
result = ''.join(s for s in pw_list) # join()을 이용하여 리스트를 문자열로 변환
print(result)