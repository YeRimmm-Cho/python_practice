N, M = map(int, input().split())

arr = [0] * N

for tc in range(M):
    i, j, k = list(map(int, input().split()))

    for x in range(i, j+1):     # 입력 인덱스와 실제 인덱스 간의 차이를 줄임 
        arr[x-1] = k

for value in arr:
    print(value, end=" ")


