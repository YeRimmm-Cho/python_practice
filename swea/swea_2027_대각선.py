n = 5  

for i in range(n):
    line = ''
    for j in range(n):
        if j == i:
            line += '#'
        else:
            line += '+'
    print(line)
