test_case = int(input())

for i in range(1, test_case+1):
    num1, num2 = map(int,input().split())
    result = 0
    if num1 > num2:
        result = '>'
    elif num1 == num2:
        result = '='
    else:
        result = '<'
    print(f"#{i} {result}")
    

