T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    k = 1
    arr = set()

    while True:
        for i in str(N*k):
            arr.add(i)
        if len(arr) == 10:
            break
        k += 1
        
        
    # 출력    
    print(f"#{tc} {N*k}")