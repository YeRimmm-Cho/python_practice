T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for r in range(N-M+1):
        for c in range(N-M+1):

            sum_fly = 0
            for x in range(r, r+M):
                for y in range(c, c+M):
                    sum_fly += arr[x][y]
            
            if sum_fly > max_v:
                max_v = sum_fly
    
    print(f"#{tc} {max_v}")