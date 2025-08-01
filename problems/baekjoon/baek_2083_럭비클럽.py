while True:
    name, age, weight = input().split()
    
    if name == '#' and int(age) == 0 and int(weight) == 0:
        break
    
    valid = ''
    if int(age) > 17 or int(weight) >= 80 :
        valid = 'Senior'
    else:
        valid = 'Junior'
    print(f"{name} {valid}")