T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(input().strip()) for _ in range(N)]    # 공백없이 입력받기
    value = 0

    mid = N // 2

    for r in range(N):
        if r <= mid:
            start = mid - r
            end = N - (mid - r)
        else:
            start = r - mid
            end = N - (r - mid)
        for c in range(start, end):
            value += int(farm[r][c])

    # 출력
    print(f"#{tc} {value}")