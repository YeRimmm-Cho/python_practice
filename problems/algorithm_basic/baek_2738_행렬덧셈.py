N, M = map(int, input().split())

A, B = [], []

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(N):
    b = list(map(int, input().split()))
    B.append(b)

for r in range(N):
    for c in range(M):
        result = A[r][c] + B[r][c]
        print(result, end=" ")
    print()

