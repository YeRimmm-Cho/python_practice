# 회원가입 유효성 검사2
# 아이디의 마지막 글자는 반드시 0부터 9 사이의 숫자로 끝나야 함
# 사용자가 입력한 아이디가 위 조건을 만족하면 True
# 그렇지 않으면 False

def is_id_valid(user_data):
    last_char = user_data['id'][-1]
    return last_char.isdigit()
 

############## 테스트 코드 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################