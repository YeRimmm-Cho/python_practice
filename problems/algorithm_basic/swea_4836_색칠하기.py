T = int(input())    # 테스트 케이스 개수
 
for tc in range(1, T+1):
    N = int(input())    # 칠할 영역의 개수
    arr = [[0]*10 for _ in range(10)]   # 10x10 격자
 
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())   # 좌상단 인덱스, 우하단 인덱스, 색
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                arr[r][c] += color  # 칠해줌
 
    # 보라색 세기
    purple = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                purple += 1
 
    print(f"#{tc} {purple}")    # 보라색이 된 칸 수