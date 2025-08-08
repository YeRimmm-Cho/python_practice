T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    test_case = int(input())
    scores = map(int, input().split())

    count = [0] * 101

    for i in scores:
        count[i] += 1

    max_value = count[0]
    max_count = 0

    for i in range(len(count)):
        if count[i] >= max_count:
            max_count = count[i]
            max_value = i
            
    print(f"#{tc} {max_value}")            