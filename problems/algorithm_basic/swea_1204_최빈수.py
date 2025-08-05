T = int(input()) # 테스트 케이스

for tc in range(1, T + 1):
    num = int(input())
    scores = list(map(int, input().split()))
    
    count = [0] * 101
    
    for value in scores:
        count[value] += 1
    
    max_count = max(count)
    mode_score = 0

    for score, c in enumerate(count):
        if c == max_count:
            mode_score = score
    
    print(f"#{tc} {mode_score}")


