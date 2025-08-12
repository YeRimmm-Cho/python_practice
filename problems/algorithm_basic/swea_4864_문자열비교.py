# T = int(input())    # 테스트 케이스

# for tc in range(1, T+1):

#     str1 = input()
#     str2 = input()

#     if str1 in str2:
#         result = 1
#     else:
#         result = 0

#     print(f"#{tc} {result}")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    result = 0
    for i in range(M - N + 1):  # str2 안에서 str1 찾기
        if str2[i:i+N] == str1:
            result = 1
            break

    print(f"#{tc} {result}")