test_case = int(input())

for i in range(1, test_case + 1):
    a, b = map(int,input().split())
    share = a // b
    remainder = a % b
    print(f"#{i} {share} {remainder}")