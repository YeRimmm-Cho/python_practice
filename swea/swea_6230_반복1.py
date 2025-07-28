score = [88, 30, 61, 55, 95]
cnt = 0
result = ''
for i in range(len(score)):
    cnt += 1
    if score[i] >= 60:
        result = '합격'
    else:
        result = '불합격'
    print(f"{cnt}번 학생은 {score[i]}점으로 {result}입니다.")