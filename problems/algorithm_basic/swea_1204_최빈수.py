T = int(input()) # 테스트 케이스

for tc in range(1, T + 1):
    num = int(input())
    scores = list(map(int, input().split()))
    
    # 0 ~ 100 => 최대값이 100

    count = [0] * 101
    
    for value in scores:
        count[value] += 1
    
    # max_count = max(count)
    # mode_score = 0

    # for score, c in enumerate(count):
    #     if c == max_count:
    #         mode_score = score
    
    max_count = count[0] # 0의 카운트를 최대 카운트로 가정
    max_score = 0 # 최대 카운트 일때의 점수를 0으로 가정.

    for i in range(len(count)):
        if count[i] > max_count:
            max_count = count[i]
            max_score = i
        
        if count[i] == max_count:
            max_score = i
    
    for i, c in enumerate(count):
        # c = count[i]
        if c > max_count:
            max_count = c
            max_score = i
        
        if c == max_count:
            max_score = i
    


    print(f"#{tc} {max_score}")


