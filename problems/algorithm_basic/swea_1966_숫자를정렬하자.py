T = int(input())

def bubble_sort(a, N):

    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = bubble_sort(arr, N)

    print(f"#{tc}", *sorted_arr)