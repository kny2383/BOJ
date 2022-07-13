T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    N, M = map(int,input().split()) # N은 영화관 자리의 열 개수, M은 영화관 한 열에 속한 좌석 개수
    if N < 12 or M < 4: print("-1") # 제한조건
    else: print(11 * M + 4) # L4의 좌석번호