arr = [list(map(int, input().split())) for _ in range(1, 10)]   # 배열 생성 => 이건 그냥 반복 횟수고 배열에 대한 것은 아님

max_v = 0
row = 0
column = 0

for r in range(len(arr)):
    for c in range(len(arr)):
        if arr[r][c] > max_v:
            max_v = arr[r][c]
            row = r
            column = c

print(max_v)
print(row+1, column+1)
    