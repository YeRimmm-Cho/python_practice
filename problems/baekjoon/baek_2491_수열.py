N = int(input().strip())
nums = list(map(int, input().split()))

inc = dec = 1
mx = 1  # 전역 최댓값
for i in range(N - 1):
    if nums[i+1] >= nums[i]:  # 비감소
        inc += 1
    else:
        inc = 1

    if nums[i+1] <= nums[i]:  # 비증가
        dec += 1
    else:
        dec = 1

    mx = max(mx, inc, dec)  # 누적 갱신

print(mx)
