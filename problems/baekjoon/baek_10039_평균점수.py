lst = []

for _ in range(5):
    score = int(input())
    lst.append(max(40, score))
    
print(sum(lst)//5)