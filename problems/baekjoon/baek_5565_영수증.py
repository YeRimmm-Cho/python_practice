total_price = int(input())

sum_price = 0
for i in range(9):
    book_price = int(input())
    sum_price += book_price
print(total_price - sum_price)