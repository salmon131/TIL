import sys
from collections import deque

queue = deque([])
arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, sys.stdin.readline().split())
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        i, j = queue.popleft()
        for dir in range(4): # 상하좌우 탐색
            nx = i + dx[dir]
            ny = j + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0: # 배열 범위 벗어나는지 확인
                arr[nx][ny] = arr[i][j] + 1
                queue.append([nx, ny])

bfs()

if any(0 in l for l in arr):
    print(-1)
else:
    print(max(map(max, arr)) - 1)