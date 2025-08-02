while True:
    string_input = input()

    if string_input == 'END':
        break
    else:
        print(string_input[::-1])