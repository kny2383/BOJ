reversed_text = [] # 뒤집힌 문장 리스트 
T = int(input()) # 테스트 케이스

for i in range(T):
    text = list(map(str,input().split())) # 문장을 단어 단위로 리스트 만들기 ex) I am happy -> ['I', 'am', 'happy']
    for j in range(len(text)):
        reversing_text = list(text[j]) # 단어별로 각각의 리스트 만들기 ex) ['I'], ['a', 'm'], ['h', 'a', 'p', 'p', 'y']
        reversing_text.reverse() # 리스트 타입에서 요소를 뒤집을 때 사용하는 reverse() 함수 ex) ['i'], ['m', 'a'], ['y', 'p', 'p', 'a', 'h']
        reversed_text.append(''.join(reversing_text)) # ex) ['i', 'ma', 'yppah']
    print(' '.join(reversed_text)) # ex) i ma yppah
    reversed_text = [] # 초기화

## 더 효율적인 코드
#T = int(input())
#for i in range(T):
#    string = list(input().split())
#    for j in string:
#        print(j[::-1], end=' ')