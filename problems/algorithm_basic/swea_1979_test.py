arr = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1]

# 정확하게 3개인 거, 2개인 거, 4개인 거 갯수 세기


cnt = 0
N = len(arr)

for i in range(N):
    if arr[i] == 1:
        cnt += 1
    else: # 1이 계속 나오다가 0으로 바뀌는 순간에 길이를 알 수 있음.
        if cnt > 0:
            print(f"=> {cnt}개 연속된 1 발견!")

        cnt = 0

    print(i, arr[i], cnt)

# for문이 끝났는데 cnt가 남아있다면 마지막 연속된 1이 남아있는 것임
if cnt > 0:
    print(f"=> {cnt}개 연속된 1 발견!")