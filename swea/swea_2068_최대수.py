# 10개의 수를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라
# 각 수는 0 이상 1000 이하의 정수이다.

test_case = int(input())

for i in range(1, test_case+1) :    # 테스트 케이스 입력
    num = list(map(int,(input().split())))  # 10개씩 입력 받음

    max_number = 0  # 테스트마다 초기화

    for n in num:
        if n > max_number:
            max_number = n

    print(f"#{i} {max_number}")
