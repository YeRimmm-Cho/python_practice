T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    N = int(input())  # 이번 케이스의 숫자 개수
    numbers = list(map(int, input().split()))
    print(min(numbers), max(numbers))
