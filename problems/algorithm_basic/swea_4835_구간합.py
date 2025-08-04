T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    lst = []
    for j in range(N - M + 1):
        lst.append(sum(arr[j:j+M]))
    print(f"#{i} {max(lst) - min(lst)}")

