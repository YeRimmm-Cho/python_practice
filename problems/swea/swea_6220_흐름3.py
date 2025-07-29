test_case = int(input())
answer = ""

for i in range(1, test_case+1):
    char = str(input())
    if char.isupper():
        answer = "대문자"
    elif char.islower():
        answer = "소문자"
    print(f"#{i} {char} 는 {answer} 입니다.")