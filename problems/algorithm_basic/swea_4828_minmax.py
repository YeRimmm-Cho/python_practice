T = int(input())

for i in range(1, T+1):     # 테스트 케이스
    N = int(input())        # 양수의 개수
    arr = list(map(int,input().split()))        # N만큼 입력받기

    max_v = arr[0]
    min_v = arr[0]

    # max 안 쓰고 풀기
    for j in arr:
        if max_v < j:
            max_v = j
        if min_v > j:
            min_v = j

    print(f'#{i} {max_v - min_v}')
