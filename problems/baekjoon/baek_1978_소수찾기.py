T = int(input())  

arr = list(map(int, input().split()))
cnt = 0

for n in arr:               # n은 값
    if n < 2:               # 0,1은 소수 아님
        continue
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:      # 나누어 떨어지면 소수 아님
            break
    else:                   # 한 번도 break 안 됨 -> 소수
        cnt += 1

print(cnt)
