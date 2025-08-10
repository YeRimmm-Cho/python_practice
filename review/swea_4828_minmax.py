T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0
    min_v = float('inf')
    for i in range(len(arr)):
        if arr[i] > max_v:
            max_v = arr[i]
        
        if arr[i] < min_v:
            min_v = arr[i]

    print(f"#{tc} {max_v - min_v}")