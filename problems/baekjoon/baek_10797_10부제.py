date = int(input())
car_numbers = list(map(int, input().split()))

cnt = 0
for num in car_numbers:
    if num == date:
        cnt += 1

print(cnt)
