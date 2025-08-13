# arr = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1]

# # 정확하게 3개인 거, 2개인 거, 4개인 거 갯수 세기


# cnt = 0
# N = len(arr)

# for i in range(N):
#     if arr[i] == 1:
#         cnt += 1
#     else: # 1이 계속 나오다가 0으로 바뀌는 순간에 길이를 알 수 있음.
#         if cnt > 0:
#             print(f"=> {cnt}개 연속된 1 발견!")

#         cnt = 0

#     print(i, arr[i], cnt)

# # for문이 끝났는데 cnt가 남아있다면 마지막 연속된 1이 남아있는 것임
# if cnt > 0:
#     print(f"=> {cnt}개 연속된 1 발견!")




T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N, K = map(int, input().split())            # 가로세로 길이 N, 단어 길이 K
    arr = [list(map(int, input().split())) for _ in range(N)]  # N*N 배열

    cnt = 0

    # 가로 검사 
    for r in range(N):
        meetzero = 0
        for c in range(N):
            if arr[r][c] == 1:
                meetzero += 1

            # 끊기는 지점
            if arr[r][c] == 0 or c == N - 1:
                if arr[r][c] == 0:
                    if meetzero == K:
                        cnt += 1
                    meetzero = 0
                else: 
                    if meetzero == K:
                        cnt += 1
                    meetzero = 0

    # 세로 검사
    for c in range(N):
        meetzero = 0
        for r in range(N):
            if arr[r][c] == 1:
                meetzero += 1

            # 끊기는 지점
            if arr[r][c] == 0 or r == N - 1:
                if arr[r][c] == 0:
                    if meetzero == K:
                        cnt += 1
                    meetzero = 0
                else:  
                    if meetzero == K:
                        cnt += 1
                    meetzero = 0

    print(f"#{tc} {cnt}")
