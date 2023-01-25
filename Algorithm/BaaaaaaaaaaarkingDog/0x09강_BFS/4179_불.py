import sys
from collections import deque

queue = deque([])
arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    arr.append(list(sys.stdin.readline().strip()))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'J':
            queue.append(['J', i, j])
        if arr[i][j] == 'F':
            queue.append(['F', i, j])

def bfs():
    while queue:
        k, i, j = queue.popleft()
        for dir in range(4): # 상하좌우 탐색
            nx = i + dx[dir]
            ny = j + dy[dir]
            if k == 'J':
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '.':
                    arr[nx][ny] = arr[i][j] + 1 if isinstance(arr[i][j], int) else 1
                    queue.append(['J', nx, ny])
            else: # 'F'
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] not in ['F', '#']:
                    arr[nx][ny] = 'F'
                    queue.append(['F', nx, ny])

bfs()
print(arr)
result = None

for i in range(0, N, N - 1):
    for j in range(M):
        if isinstance(arr[i][j], int):
            result = min(arr[i][j], result) if result else arr[i][j]

for i in range(N):
    for j in range(0, M, M - 1):
        if isinstance(arr[i][j], int):
            result = min(arr[i][j], result) if result else arr[i][j]

if result:
    print(result + 1)   
else:
    print('IMPOSSIBLE')