# 성공적인 공연기획

# 목표: 모든 사람이 기립박수

# 기립 박수를 하는 조건: "지금 기립 박수하고 있는 사람의 수" >= 특정한 수
# => 위 조건을 만족해야 기립 박수를 함.


# 아무런 조건없이 기립 박수하는 사람도 있음

# 각 사람들이 기립 박수를 하려면 최소 몇 명(특정한 수)의 사람이 기립 박수를 해야 하는지 조사했음


# 입력 : 0부터 9 사이의 문자로 이루어진 문자열
# 첫번째 글자의 의미: 기립 박수를 하고 있는 사람이 아무도 없을 때 (0명일 때) 기립 박수를 하는 사람 수
# i번째 글자는: 지금 기립 박수를 하고 있는 사람이 i-1명일 때 기립 박수를 하는 사람의 수
# 가장 마지막 문자는 0이 아님


T = int(input())

for tc in range(1, T+1):
    conditions = list(map(int, input().strip()))
    
    people = 0  # 현재 박수치고 있는 사람 수
    result = 0  # 고용할 사람 수

    for i in range(len(conditions)):
        # i 뜻: i명 이상이면 conditions[i]명의 사람이 박수를 친다.
        if people < i:
            result += i - people # 부족한 숫자만큼 더 고용
            people += i - people # 그 사람 수만큼 고용했다고 가정하고 현재 인원 늘리기

        
        people += conditions[i]


    print(f"#{tc} {result}")