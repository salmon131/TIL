import sys

N, K = map(int, sys.stdin.readline().strip().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))

dp = [0] * (K + 1)
dp[0] = 1
for i in range(N):
    for j in range(coin[i], K + 1):
        dp[j] += dp[j - coin[i]]

print(dp[K])        
