"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

V = int(input()) # "13"
arr = list(map(int, input().split())) # "2 1 2 3 1 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13"

print(len(arr))

E = V-1 # 간선의 수

left = [0] * (V+1)
right = [0] * (V+1)

for i in range(E):
    print(i*2, i*2+1)
    p = arr[i*2] # 부모
    c = arr[i*2+1] # 자식

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

print(left)
print(right)