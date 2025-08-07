# 리스트 오름차순으로 버블 정렬
def bubble_sort(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = bubble_sort(arr[:])

    result = []
    left = 0            # 처음 인덱스
    right = N - 1       # 맨 끝 인덱스

    while len(result) < 10 and left <= right:   # 종료 조건
        result.append(sorted_arr[right])
        right -= 1      # 끝에서부터

        if len(result) < 10:
            result.append(sorted_arr[left])
            left += 1    # 시작부터

    print(f"#{tc}", *result)        # result 값 모두
