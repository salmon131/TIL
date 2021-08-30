'''my code'''
def solve(a):
    return sum(a)

'''time test'''
# for문으로 합을 구했을 경우와 수행 시간 비교
import timeit
import numpy as np
data=np.random.rand(100)
# print(data)

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
