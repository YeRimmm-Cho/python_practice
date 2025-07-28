# 전체 점수 중 최저점을 반환하는 min_score 함수를 완성하시오.
# input과 min은 사용하지 않기
def min_score(scores):
    minscore = scores[0]
    for i in scores:
        if i < minscore:
            minscore = i
    return minscore

############## 테스트 코드 #################
print(min_score([30, 60, 90, 70])) # 30
print(min_score([0, 10, 20, 30, 40, 50])) # 0
print(min_score([50, 70, 50, 45, 80, 80])) # 45
#####################################################

# 테스트 코드는 이곳에
print(min_score([100, 100]))  