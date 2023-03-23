import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y, depth):
    queue = deque()
    queue.append([x, y])
    vis[x][y] = 1
    while queue:
        i, j = queue.popleft()
        for dir in range(4):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] <= depth or vis[nx][ny]:
                continue
            vis[nx][ny] = 1
            queue.append([nx, ny])

max_cnt = 0
for depth in range(101):
    cnt = 0
    vis = []
    vis = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > depth and vis[i][j] == 0:
                bfs(i, j, depth)
                cnt += 1
    if cnt == 0: # 모든 지역 물에 잠김
        break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)