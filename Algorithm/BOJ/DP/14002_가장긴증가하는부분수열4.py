import sys

'''My Ans. 각 위치에서의 최장 부분수열을 모두 저장함
6
10 20 10 30 20 50
[[10], [20], [10], [30], [20], [50]]
[[10], [10, 20], [10], [30], [20], [50]]
[[10], [10, 20], [10], [30], [20], [50]]
[[10], [10, 20], [10], [10, 20, 30], [20], [50]]
[[10], [10, 20], [10], [10, 20, 30], [10, 20], [50]]
[[10], [10, 20], [10], [10, 20, 30], [10, 20], [10, 20, 30, 50]]
'''
N = int(sys.stdin.readline().strip())
arr = [int(num) for num in sys.stdin.readline().split()]

dp = [1] * N
dp_arr = [[arr[i]] for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            dp_arr[i] = dp_arr[j] + [arr[i]]
    # print(dp_arr)
res = max(dp)
res_idx = dp.index(res)
print(res)
print(' '.join(map(str, dp_arr[res_idx])))


'''Other Ans. 각 위치에서 부분수열의 최댓값의 인덱스를 저장하고 출력시에는 재귀를 활용하여 거꾸로 올라감
6
10 20 10 30 20 50
 ㄴ  ㄴ ㄴ  ㄴ    ㅣ
   \  \  \   \  ㅣ
    |   \ \   \ |
    ㅣ    \ \  \ㅣ
-1  0 -1  1  2  3
'''
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1]*(N)
dpIdx = [-1]*(N)
for i in range(N):
    m = 0
    idx = -1    
    for j in range(i-1, -1, -1):
        if(arr[i] > arr[j] and m < dp[j]):
            m = dp[j]
            idx = j
    dp[i] += m
    dpIdx[i] = idx    
print(max(dp))

# print(dp)
# print(dpIdx)

def putAns(idx):
    if(dpIdx[idx] == -1):
        print(arr[idx], end=" ")
        return
    putAns(dpIdx[idx])
    print(arr[idx], end=" ")
    
putAns(dp.index(max(dp)))