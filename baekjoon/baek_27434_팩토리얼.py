N = int(input())
result = 1

for i in range(1, N + 1):
    result *= i
print(result)

# 아래 함수 호출은 runtime error
# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * factorial(number - 1)
# print(factorial(N))

# 이유
# 입력 N이 재귀 호출 한도를 넘어서 들어올 수 있어서