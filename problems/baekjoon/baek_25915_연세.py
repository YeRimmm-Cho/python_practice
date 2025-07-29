char = input()
password = 'ILOVEYONSEI'
result = 0

for i in range(len(password)):
    result += abs(ord(password[i]) - ord(char))
    char = password[i]

print(result)