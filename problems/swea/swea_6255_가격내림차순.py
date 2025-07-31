stock = {"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000,}

# 값 기준 내림차순 정렬
sorted_stock = sorted(stock.items(), key=lambda x: x[1], reverse=True)

# 출력
for name, price in sorted_stock:
    print(f"{name}: {price}")
