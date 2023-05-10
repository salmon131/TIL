import sys

N, K = map(int, sys.stdin.readline().strip().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))

dp = [10001] * (K + 1)
dp[0] = 0
for i in range(N):
    for j in range(coin[i], K + 1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])        
