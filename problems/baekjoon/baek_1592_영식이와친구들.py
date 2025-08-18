N, M, L = map(int, input().split())

arr = [0] * N
player = 0
arr[player] = 1
throw = 0

while arr[player] < M:
    if arr[player] % 2 == 1:
        player = (player + L) % N
    else:
        player = (player - L) % N

    arr[player] += 1    
    throw += 1

print(throw)
