T = int(input())

for tc in range(1, T+1):

    N = int(input())              # 카드 장수
    numbers = list(map(int, input().strip()))  # 공백 없이 붙은 숫자들
    counts = [0] * 10             # 0~9 빈도
    
    max_count = -1
    max_card = -1

    for card in range(10):
        if counts[card] >= max_count:
            max_count = counts[card]
            max_card = card

    print(f"#{tc}")