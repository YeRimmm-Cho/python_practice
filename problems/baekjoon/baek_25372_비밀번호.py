test_case = int(input())

for _ in range(test_case):
    password = input()
    password_length = len(password)

    if 6 <= password_length <= 9:
        print('yes')
    else:
        print('no')
