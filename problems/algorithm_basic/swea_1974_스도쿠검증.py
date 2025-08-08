T = int(input())
for tc in range(1, T + 1):
    box = [list(map(int, input().split())) for _ in range(9)]
    valid = 1 

    # 행 검사
    for row in box:
        if len(set(row)) != 9:  # 중복이 있다면
            valid = 0
            break

    # 열 검사
    if valid:
        for c in range(9):
            col = []
            for r in range(9):
                col.append(box[r][c])

            if len(set(col)) != 9:
                valid = 0
                break

    # 3x3 검사
    if valid:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []

                for r in range(3):
                    for c in range(3):
                        square.append(box[i + r][j + c])    # 기준점 + 상대 좌표

                if len(set(square)) != 9:
                    valid = 0
                    break

    print(f"#{tc} {valid}")
