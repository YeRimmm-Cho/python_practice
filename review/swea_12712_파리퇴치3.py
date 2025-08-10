T = int(input())

# 상하좌우 델타
dr_plus = [-1, 1, 0, 0]
dc_plus = [0, 0, -1, 1]

# 대각선 델타
dr_multi = [-1, -1, 1, 1]
dc_multi = [-1, 1, -1, 1]


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for r in range(N):
        for c in range(N):
            sum_fly = arr[r][c] # 기준점 잡기

            # 상하좌우 검사
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr_plus[d] * m 
                    nc = c + dc_plus[d] * m 

                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]
            
            # 최댓값
            if sum_fly > max_v:
                max_v = sum_fly

            
            # 대각선 검사
            sum_fly = arr[r][c] # 기준점 다시 초기화
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr_multi[d] * m 
                    nc = c + dc_multi[d] * m 

                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]
            
            # 최댓값
            if sum_fly > max_v:
                max_v = sum_fly
    
    print(f"#{tc} {max_v}")