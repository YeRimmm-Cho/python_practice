import copy

catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

backup_catalog = copy.deepcopy(catalog)

catalog[3][0] = '성공을 향한 한 걸음'
catalog[3][1] = '내 삶의 변화'
catalog[3][-1] = '목표 달성의 비밀'


print('catalog와 backup_catalog를 비교한 결과')
print(catalog is backup_catalog)

print(f'backup_catalog:\n {backup_catalog}\n')
print(f'catalog:\n {catalog}')
