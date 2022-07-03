T = int(input())
reversed_text = []
result_text = []
for i in range(T):
    text = list(map(str,input().split()))
    for j in range(len(text)):
        reversing_text = list(text[j])
        reversing_text.reverse()
        reversed_text.append(''.join(reversing_text))
    print(' '.join(reversed_text))
    reversed_text = []