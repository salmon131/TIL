import sys

N = int(sys.stdin.readline().strip())
dp = [0] * 91

# top-down 방식
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibo(n-2) + fibo(n-1)
    return dp[n]

print(fibo(N))

# bottom-up 방식
dp[0] = 0
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])