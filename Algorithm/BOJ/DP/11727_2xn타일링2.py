import sys
import operator as op
from functools import reduce

# '''Try 1. DP 알고리즘을 적용하지 않음
# '''
# def nCr(n, r):
#     if n < 1 or r < 0 or n < r:
#         raise ValueError
#     r = min(r, n-r)
#     numerator = reduce(op.mul, range(n, n-r, -1), 1)
#     denominator = reduce(op.mul, range(1, r+1), 1)
#     return numerator // denominator

# N = int(sys.stdin.readline().strip())
# arr = [i for i in range(N//2, 0, -1)]
# result = 1
# for i, j in enumerate(arr):
#     result += nCr(arr[0]+i, j) * 2**j

# print(result%10007)

'''Try 2. DP 알고리즘 적용 후
'''
def solution(n):
    dp = [0 for i in range(n)]
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n-1]

N = int(sys.stdin.readline().strip())
arr = [i for i in range(N//2, 0, -1)]
result = 1
for i, j in enumerate(arr):
    result += nCr(arr[0]+i, j) * 2**j

print(result%10007)