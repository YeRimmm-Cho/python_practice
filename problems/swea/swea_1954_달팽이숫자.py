T = int(input())

# 방향 벡터 (우, 하, 좌, 상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    
    snail = [[0] * N for _ in range(N)]

    # 시작 위치 및 방향 (맨 처음은 우측으로 이동)
    r, c, d = 0, 0, 0
    cnt = 1
    snail[r][c] = cnt

    while cnt < N * N:
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            cnt += 1
            snail[nr][nc] = cnt
            r, c = nr, nc
        else:
            d = (d + 1) % 4
    
    # 결과 출력
    print(f"#{tc}")
    for row in snail:
        print(" ".join(map(snail, row)))

    