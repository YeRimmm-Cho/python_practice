number_list = []

for i in range(9):
    number_input = int(input())
    number_list.append(number_input)

print(max(number_list))
print(number_list.index(max(number_list)) + 1)