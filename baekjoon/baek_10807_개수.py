import sys

test_case = int(sys.stdin.readline())  
num_list = list(map(int, sys.stdin.readline().split()))  
input_num = int(sys.stdin.readline())  
print(num_list.count(input_num))
