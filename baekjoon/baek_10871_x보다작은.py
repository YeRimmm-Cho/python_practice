import sys

test_case, X = map(int, sys.stdin.readline().split())

a_list = list(map(int, sys.stdin.readline().split()))

for num in a_list:
    if num < X:
        print(num, end=' ')
