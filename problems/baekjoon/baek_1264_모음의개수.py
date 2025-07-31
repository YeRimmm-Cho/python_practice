while True:
    string_input = input()
    if string_input == '#':
        break
    cnt = 0
    for i in string_input.lower():
        if i in 'aeiou':
            cnt += 1
    print(cnt)