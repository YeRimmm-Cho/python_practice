test_case = int(input())

for i in range(1, test_case+1):
    num = list(map(int, input().split()))
    avg = sum(num) / len(num)
    result_avg = round(avg)

    print(f"#{i} {result_avg}")