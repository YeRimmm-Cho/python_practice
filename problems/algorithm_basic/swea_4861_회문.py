def palin(arr, N, M):

    # 가로
    for r in range(N):
        row = arr[r]

        for c in range(N-M+1):
            word = row[c: c+M]

            if word == word[::-1]:
                return word

    # 세로
    for c in range(N):
        column = ""

        for r in range(N):
            column += arr[r][c]

        for r in range(N-M+1):
            word = column[r: r+M]
            if word == word[::-1]:
                return word


T = int(input())    # 테스트 케이스
for tc in range(1, T+1):
    N, M = map(int, input().split())

    array = [input() for _ in range(N)]
    find_word = palin(array, N, M)

    print(f"#{tc} {find_word}")
