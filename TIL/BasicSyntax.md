# 파이썬 문제 풀 때 헷갈린 개념 정리 (Basic Syntax)

## 1. 딕셔너리 순회 패턴
파이썬에서 딕셔너리는 `for`문으로 순회 시 기본적으로 **key만** 반환한다.
<br></br>
### 자주 쓰는 패턴

| 목적              | 문법                        | 결과 예시                |
|-------------------|-----------------------------|--------------------------|
| **키만 순회**       | `for k in d:`<br>`for k in d.keys():` | `'name'`, `'age'`        |
| **값만 순회**       | `for v in d.values():`      | `'Alice'`, `25`          |
| **키와 값 동시에**   | `for k, v in d.items():`    | `('name', 'Alice')`, `('age', 25)` |

<br></br>

## 추가 유용 메서드
- `d.get(key, default)` → 키 없으면 `default` 반환
- `d.setdefault(key, default)` → 키 없으면 추가하고 기본값 반환
- `key in d` → 딕셔너리에 키 존재 여부 확인

<br></br>
<br></br>

## 2. 값 vs 인덱스 구분
- `for i in lst:` → **i는 값**
- `for i in range(len(lst)):` → **i는 인덱스**
- 둘 다 필요하면:
```python
for idx, val in enumerate(lst):
    print(idx, val)
```

<br></br>
<br></br>

## 3. 가변/불변 객체와 메서드

### 리스트(list): 가변  
  - 주요 메서드: `append()`, `extend()`, `remove()`, `sort()`, `reverse()`  
  - 특징: 제자리 변경, 반환값 없음
<br></br>
### 문자열(str) & 튜플(tuple): 불변  
  - 값을 직접 바꿀 수 없음 → **새 객체를 반환해야 함**
  <br></br>

### 정렬
- **제자리 정렬:** `lst.sort()` (리스트 전용)
- **새 정렬 반환:** `sorted(iterable)` (모든 시퀀스 가능)

<br></br>
<br></br>

## 4. 문자열 메서드 활용
### 자주 쓰는 메서드
- s.strip() → 앞뒤 공백 제거

- s.isdigit() → 숫자만 있는지 검사

- s.isalpha() → 알파벳만 있는지 검사

- s.isspace() → 공백 문자만 있는지 검사    
<br></br>

**인덱싱 / 슬라이싱**
```python
s[-1]   # 마지막 글자
s[1:4]  # 1 ~ 3번째 글자
```
<br></br>
**자주 한 실수**
- 빈 문자열 검사에 .isspace() 사용 → 실패 (''은 False)
- .index()를 인덱싱처럼 사용 → AttributeError