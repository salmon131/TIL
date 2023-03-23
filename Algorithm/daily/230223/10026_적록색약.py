import sys
from collections import deque

N = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
vis = [[0] * N for _ in range(N)]
queue = deque()

three_cnt, two_cnt = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue.append([x, y])
    vis[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]==arr[x][y] and not vis[nx][ny]:
                vis[nx][ny] = 1
                queue.append([nx, ny])

# 적록색약 아닌 경우
for i in range(N):
    for j in range(N):
        if vis[i][j] == 0:
            bfs(i, j)
            three_cnt += 1

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

vis = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if vis[i][j] == 0:
            bfs(i, j)
            two_cnt += 1

print(three_cnt, two_cnt)