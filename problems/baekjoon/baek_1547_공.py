M = int(input())    # 컵의 위치를 바꾼 횟수

arr = [0, 1, 0, 0]

for i in range(M):
    
    X, Y = map(int, input().split())
    arr[X], arr[Y] = arr[Y], arr[X]

for k in range(1, 4):
    if arr[k] == 1:
        print(k)
        break