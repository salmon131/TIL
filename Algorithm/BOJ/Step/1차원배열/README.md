*(2562_최댓값 문제 中)*

**# 임의의 개수의 정수를 n줄 입력받아 1차원 리스트에 저장**

```
data = []
for i in range(9):
    data.append(int(input()))
```
🗸 `input()`의 입력은 마지막 개행문자(\n)를 포함하지 않는다.

---
**# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장**
```
import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
```
🗸 `sys.stdin.readline()`
* 여러줄을 입력받는 상황에서 사용
* `input()`과 달리 마지막 개행문자(\n)를 포함하기 때문에 `split()`으로 제거해주어야한다.

🗸 `split()`은 문자열을 나눠주는 함수

- 괄호 안에 특정 값을 넣어주면 그 값을 기준으로 문자열을 나누고, 아무 값도 넣어주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 나눈다.

🗸 `list()`는 자료형을 리스트형으로 변환해주는 함수

- `map()`은 맵 객체를 만들기 때문에, 리스트형으로 바꿔주기 위해서 list()로 감싸준다.

---
*(3052_나머지 문제 中)*

**# list에서 distinct한 원소 갯수 세기**

🗸 `set type`으로 변경해주면 된다.
* 단 set은 indexing이 안되는 등의 제약사항이 있기 때문에 다시 `list`로 돌려주는 것이 좋다.

---
*(8959_OX퀴즈 문제 中)*

**# list를 groupby하여 반복되는 문자열 찾기**

result =  "OOXXOXXOOO" 일때,
```
from itertools import groupby

for k, g in groupby(result):
    print(k)
    print(list(g))
```
 위의 결과는 다음과 같다.
```
O
['O', 'O']
X
['X', 'X']
O
['O']
X
['X', 'X']
O
['O', 'O', 'O']
```
---
*(4344_평균은 넘겠지 문제 中)*

**# 소수점 이하 N번째 자리까지 출력하기**

🗸 `round()`함수는 소수점 끝자리가 0이면 출력을 하지 않는다.
* 소수점 이하 3째자리 까지 출력해도 40.000% 가 아니라 40.0%로 출력한다.

🗸 따라서 `format` 메소드를 사용하여 서식을 지정하자
```
# test
print("{}%".format(round(40.000, 3)))
print("{:.3f}%".format(40.0000))
print("{:.3f}%".format(40.6664))
print("{:.3f}%".format(40.6666))

# 출력 결과
40.0%
40.000%
40.666%
40.667%
```