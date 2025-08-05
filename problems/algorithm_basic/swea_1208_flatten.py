for i in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    
    for j in range(dump):
        max_h = max(box)
        min_h = min(box)

        maxIdx = box.index(max_h)
        minIdx = box.index(min_h)

        box[maxIdx] -= 1
        box[minIdx] += 1

    result = max(box) - min(box)
    print(f"#{i} {result}")
