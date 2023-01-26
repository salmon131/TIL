import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque([])
vis = [0] * 100001

def bfs():
    cnt = 0
    queue.append(N)
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if x == K:
                return cnt
            if x > 100000 or x < 0:
                continue
            if vis[x]: # 방문했던 곳인지 확인
                continue
            vis[x] = 1
            if x > K:
                queue.append(x - 1)
            else:
                queue.append(x + 1)
                queue.append(x - 1)
                queue.append(x * 2)
        cnt += 1
                
print(bfs())

