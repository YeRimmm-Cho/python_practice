total_money = int(input())
total_category = int(input())
result = 0

for i in range(1, total_category + 1):
    money, stock = map(int, input().split())
    result += money * stock

if total_money == result:
    print('Yes')
else:
    print('No')