T = int(input())    # 테스트 케이스

for tc in range(1, T+1):

    C = input()     # 문자열 입력 받기
    stack = []

    for ch in C:
        if stack and stack[-1] == ch:   # 문자 반복되면
            stack.pop()
        else:
            stack.append(ch)

    # 출력
    print(f"#{tc} {len(stack)}")