x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for x in x_list:
    if x_list.count(x) == 1:
        x4 = x
        
for y in y_list:
    if y_list.count(y) == 1:
        y4 = y

print(x4, y4)
