T = int(input())

for i in range(1, T+1):
    N = int(input())    # 카드 장수 N
    num = list(map(int, input()))   # N개의 숫자

    cnt = [0] * 10  # 장수 세는 리스트
    idx_num = 0     # 장수
    max_num = 0     # 최대수

    for card in num:
        cnt[card] += 1

    for j in range(len(cnt)):
        if cnt[j] >= idx_num:   
            max_num = j
            idx_num = cnt[j]


    print(f"#{i} {max_num} {idx_num}")