T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_v = 0       
    for r in range(N - M + 1):
        for c in range(N - M + 1):

            total = 0   # 파리
            for x in range(r, r+M):     # M에서 돌기
                for y in range(c, c+M):
                    total += arr[x][y]

            if max_v < total:
                max_v = total
            
    print(f"#{tc} {max_v}")

