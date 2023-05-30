import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])
arr = []
vis = [[0]*N for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            queue.append([i, j])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        i, j = queue.popleft()
        for dir in range(4): # 상하좌우 탐색
            nx = i + dx[dir]
            ny = i + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] == 1:
                queue.append([nx, ny])

bfs()

print(arr)