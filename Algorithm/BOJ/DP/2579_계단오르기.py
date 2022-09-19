import sys

'''my code - failed'''
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
arr = arr[::-1] # 계단 순서 뒤집기
result = arr[0] # 마지막 계단 숫자 더하고 시작

idx = 0
while idx < len(arr) - 1:
    if idx == len(arr) - 2: # 두 번째 계단이면 첫 번째 계단 더하고 종료
        result += arr[idx+1]
        break
    if arr[idx+1] > arr[idx+2]:
        result += arr[idx+1]
        idx += 1
    else:
        result += arr[idx+2]
        idx += 2

print(result)

'''develope code'''
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
dp = []

dp.append(arr[0]) # dp[0]
if N >= 2:
    dp.append(max(arr[0] + arr[1], arr[1])) # dp[1]
if N >= 3:
    dp.append(max(arr[0] + arr[1], arr[1] + arr[2])) # dp[2]
for i in range(3, N):
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]))

print(dp[-1])

