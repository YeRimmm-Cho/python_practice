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
