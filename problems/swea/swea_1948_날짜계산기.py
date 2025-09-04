T = int(input())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):

    m1, d1, m2, d2 = map(int, input().split())

    sum_1 = sum(days[:m1]) + d1
    sum_2 = sum(days[:m2]) + d2

    result = sum_2 - sum_1 + 1

    print(f"#{tc} {result}")
