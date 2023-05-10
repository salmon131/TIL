import sys

N = int(sys.stdin.readline().strip())
arr = [int(num) for num in sys.stdin.readline().split()]
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))