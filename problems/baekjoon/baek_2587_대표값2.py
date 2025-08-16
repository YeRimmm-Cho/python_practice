arr = []
for _ in range(5):
    N = int(input())
    arr.append(N)
arr.sort()
print(sum(arr) // 5)
print(arr[2])