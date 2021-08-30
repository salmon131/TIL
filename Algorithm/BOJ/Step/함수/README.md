*(155962_정수N개의합 문제 中)*

**# 1차원 list 원소의 합은 for문보다 sum()이 빠르다**

난수를 생성하여 list를 생성한 후 수행시간을 비교해 보았다.
```
import numpy as np
data=np.random.rand(100)
```
🗸 `sum()` 내장함수 이용
```
def solve(a):
    return sum(a)
```
🗸 `for문` 이용
```
result = 0
for x in data:
    result += x
```
전체 코드
```
# 1. sum()사용
start = timeit.default_timer()
result = solve(data)
stop = timeit.default_timer()
print(f"sum 수행시간 : {stop - start:0.6f}")

# 2. for문 사용
start = timeit.default_timer()
result = 0
for x in data:
    result += x
stop = timeit.default_timer()
print(f"for 수행시간 : {stop - start:0.6f}")
```
실행 결과
```
sum 수행시간 : 0.000015
for 수행시간 : 0.000046
```
주의할 점

🗸 2차원 이상의 list의 경우 `sum()`을 사용하면 TypeError가 발생한다.

---

(진행 중)