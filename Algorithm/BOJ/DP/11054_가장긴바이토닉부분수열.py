import sys

'''Try 1. 이중반복 내에서 LIS, LDS를 사용함 - 시간초과
'''
N = int(sys.stdin.readline().strip())
arr = [int(num) for num in sys.stdin.readline().split()]

def LIS(arr: list) -> int:
    # 가장 긴 부분증가 수열을 구한다.
    # 단, 마지막 수가 최대여야한다. 
    l_arr = [n for n in arr if n <= arr[-1]]
    l_dp = [1] * len(l_arr)
    for i in range(1, len(l_arr)):
        for j in range(i):
            if l_arr[i] > l_arr[j]:
                l_dp[i] = max(l_dp[i], l_dp[j] + 1)
    return max(l_dp)

def LDS(arr: list) -> int:
    # 가장 긴 부분감소 수열을 구한다.
    # 단, 처음 수가 최대여야한다. 
    r_arr = [n for n in arr if n <= arr[0]]
    r_dp = [1] * len(r_arr)
    for i in range(1, len(r_arr)):
        for j in range(i):
            if r_arr[i] < r_arr[j]:
                r_dp[i] = max(r_dp[i], r_dp[j] + 1)
    return max(r_dp)


# 가장 긴 바이토닉 수열을 구한다.
# 가장 긴 부분증가 수열 + 가장 긴 부분 감소 수열 - 1
dp = [1] * N

for i in range(1, N):
    maxed = 0
    for j in range(i + 1):
        lis = LIS(arr[:j+1])
        lds = LDS(arr[j:i+1])
        bitonic_len = lis + lds - 1
        maxed = max(maxed, bitonic_len)
    dp[i] = maxed
print(dp[-1])

'''Try 2. LIS, LDS를 한 번씩만 사용해야함 -  성공'''
N = int(sys.stdin.readline().strip())
arr = [int(num) for num in sys.stdin.readline().split()]

dp_lis = [1] * N
dp_lds = [1] * N
dp_bitonic = [0] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_lis[i] = max(dp_lis[i], dp_lis[j] + 1)

arr.reverse()

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_lds[i] = max(dp_lds[i], dp_lds[j] + 1)

dp_lds.reverse()

for i in range(N):
    dp_bitonic[i] = dp_lis[i] + dp_lds[i] - 1

print(max(dp_bitonic))
