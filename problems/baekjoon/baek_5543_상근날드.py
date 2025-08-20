up_burger = int(input())
mid_burger = int(input())
down_burger = int(input())
coke = int(input())
cider = int(input())
price = min(up_burger, mid_burger, down_burger)+min(coke, cider) - 50
print(price)