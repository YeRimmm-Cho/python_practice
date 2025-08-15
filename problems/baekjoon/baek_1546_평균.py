N = int(input())

scores = list(map(int, input().split()))
M = max(scores)
new_sum = 0

for i in range(N):
    new_sum += scores[i] / M * 100

print(new_sum/N) 