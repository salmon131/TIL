import sys

'''Try 1. 이중반복 사용하지 않음 (실패)
반례 : 2 1 5 6 7
예상 답: 20
출력 답: 19
'''
N = int(sys.stdin.readline().strip())
arr = [int(num) for num in sys.stdin.readline().split()]
dp = []
min_idx = 0

dp.append(arr[0]) # dp[0]
for i in range(1, N):
    if arr[i] > arr[i-1]:
        dp.append(dp[i-1] + arr[i])
        continue
    if arr[min_idx] > arr[i]: # 현재 수 이전에 더 작은 수가 없는 경우
        dp.append(arr[i])
    else:
        dp.append(dp[min_idx] + arr[i])
        min_idx = i

print(max(dp))

'''Try 2. 이중반복 사용 (성공)'''
N = int(sys.stdin.readline().strip())
arr = [int(num) for num in sys.stdin.readline().split()]
dp = []

dp.append(arr[0]) # dp[0]
for i in range(1, N):
    maxed = 0
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i] and maxed < dp[j]:
            maxed = dp[j]
    dp.append(arr[i] + maxed)

print(max(dp))