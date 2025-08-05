"""

for 변수 in 반복가능한것:
    변수에 대해 반복

- 반복가능한 것(iterable)에서 하나씩 꺼내서 변수에 넣는다.
- iterable: 리스트, 문자열, 튜플, range(), ..

- range(N): 0, 1, 2, ... , N-1까지 반복
- 인덱스를 사용하려면 range()를 사용해야 함

- 리스트의 원소가 N개가 있다면: 인덱스는 0, 1, 2, ..., N-1까지 있음.
- 리스트 원소의 개수: len(arr) = N
"""

arr = [3, 4, 2, 1, 7] # 

for num in arr:
    print(num)
# idx 굳이 필요 없고, 그냥 원소의 값만 얻어오면 되는 경우.

for i in range(len(arr)):
    print(i, arr[i])
# idx, 원소의 값 둘다 필요한 경우.

for i in range(5):
    print(i, arr[i])