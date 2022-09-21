import sys

N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
dp = []

dp.append(arr[0]) # dp[0]
if N > 1:
    dp.append(arr[0] + arr[1]) # dp[1]
if N > 2:
    dp.append(max(arr[0] + arr[2], arr[1] + arr[2], dp[1])) # dp[2]
for i in range(3, N):
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i], dp[i-1]))

print(dp[-1])

