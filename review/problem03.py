# 회원가입 유저 정보 유효성 검사
# 아이디와 비밀번호 중 하나라도 비어있는 문자열이면 False, 그렇지 않으면 True


def is_user_data_valid(user_data):
    for i in user_data.values():
        if i =='':
            return False
        else:
            return True


############## 테스트 코드 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################