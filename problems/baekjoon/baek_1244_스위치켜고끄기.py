# 스위치 켜고 끄기
N = int(input())        # 스위치 개수
switch_lst = [0] + list(map(int, input().split()))   # 스위치 상태
student = int(input())  # 학생 수

for _ in range(student):
    gender, number = map(int, input().split())


    if gender == 1:     # 남학생
        for k in range(1, N+1):
            if k % number == 0:     # 배수라면
                switch_lst[k] = 1 - switch_lst[k]       # 스위치 상태 바꿈

    else:       # 여햑생
        
        switch_lst[number] = 1 - switch_lst[number]       # 해당 번호는 무조건 바뀜
        
        i = 1       # 스위치 번호는 1부터 시작
        while number - i >= 1 and number + i <= N:      # 범위 안에서

            if switch_lst[number-i] == switch_lst[number+i]:    # 대칭되는 두 번호가 같으면
                switch_lst[number-i] = 1 - switch_lst[number-i]
                switch_lst[number+i] = 1- switch_lst[number+i]

            else:
                break

            i += 1

# 출력
for i in range(1, N + 1):
    print(switch_lst[i], end=' ')
    if i % 20 == 0:
        print()