import sys
case = (int(sys.stdin.readline()))

for i in range(1, case + 1):
    print(' '*(case-i),end='')
    print('*'*i)