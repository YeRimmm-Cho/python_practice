number = int(input())
numlist = 0

for i in range(1, number + 1):
    if number % i == 0:
        numlist += 1
        print(f"{i}(은)는 {number}의 약수입니다.")
        if numlist == 2:
            print(f"{number}(은)는 1과 {number}로만 나눌 수 있는 소수입니다.")
