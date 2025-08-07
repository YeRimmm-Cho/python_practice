T = int(input())    # 테스트  케이스

# 상하좌우 델타
dr_plus = [-1, 1, 0, 0]
dc_plus = [0, 0, -1, 1]

# 대각선 델타
dr_multi = [-1, -1, 1, 1]
dc_multi = [-1, 1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]   # N*N 배열 생성

    max_v = 0 # 합의 최대값
    # 반복을 돌기 전에 미리 초기화
    # 최대값을 구할 때는 최소값으로 초기화
    # 최소값을 구할 때는 최대값으로 초기화

    # max_v = float('inf') # 무한대 최대
    # min_v = -float('inf') # 무한대 최소

    for r in range(N):      # 기준점 잡기
        for c in range(N):
            # (r, c)가 정해질 때마다 합이 생김.

            # + 방향 합 구하기
            sum_fly = arr[r][c]

            # + 방향 탐색
            for d in range(4):
                for m in range(1, M):  # M 만큼의 방향
                    nr = r + dr_plus[d] * m
                    nc = c + dc_plus[d] * m 
                    
                    if 0 <= nr < N and 0 <= nc < N:     # 범위 안에 있다면
                        sum_fly += arr[nr][nc]

            if sum_fly > max_v:
                max_v = sum_fly

            
            # * 방향 합 구하기
            sum_fly = arr[r][c]


            # * 방향 탐색
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr_multi[d] * m
                    nc = c + dc_multi[d] * m 

                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]

            if sum_fly > max_v:
                max_v = sum_fly

    
    print(f"#{tc} {max_v}")