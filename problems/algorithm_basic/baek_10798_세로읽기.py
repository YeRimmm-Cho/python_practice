arr = []

for tc in range(5):
    txt = input()   # 문자열 5번 입력받기
    arr.append(txt)

for c in range(15):     # 최대 15글자
    for r in range(5):
        if c < len(arr[r]):
            print(arr[r][c], end ='')
