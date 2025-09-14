T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 당근 개수
    carrots = list(map(int, input().split()))   # 당근 리스트
    cnt = 1     # 연속하는 길이 구간
    max_cnt = 0     # 최대값 비교

    for i in range(N-1):
        if carrots[i+1] > carrots[i]:
            cnt += 1
        else:
            cnt = 1

        if max_cnt < cnt:
            max_cnt = cnt

    # 출력
    print(f"#{tc} {max_cnt}")