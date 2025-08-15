N = int(input())
arr = []
for i in range(N):
    number = int(input())
    arr.append(number)

def bubble (array, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
    return array

bubble(arr, N)
for k in arr:
    print(k)