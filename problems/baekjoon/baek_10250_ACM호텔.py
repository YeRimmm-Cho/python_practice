T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())

    floor = N % H
    if floor == 0:  # 꼭대기 층일 때
        floor = H
    
    room = (N - 1) // H + 1

    result = floor * 100 + room
    print(result)