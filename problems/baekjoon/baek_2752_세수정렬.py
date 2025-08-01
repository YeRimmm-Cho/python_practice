A, B, C = map(int,input().split())

lst = []
lst.append(A)
lst.append(B)
lst.append(C)

for i in sorted(lst):
    print(i, end=" ")