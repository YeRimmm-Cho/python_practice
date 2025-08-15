N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())
    
    basket[i-1:j] = basket[i-1:j][::-1] # 범위를 1 ~ N+1로 해서 i-1

print(*basket)