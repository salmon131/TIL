import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
vis = [[0] * col for _ in range(row)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
arr = []
for _ in range(row):
    arr.append(list(map(int, sys.stdin.readline().split())))

def bfs(i, j):
    area = 1
    vis[i][j] = 1 # 방문 표시
    queue.append([i, j])
    while queue:
        i, j = queue.popleft()
        for dir in range(4):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if arr[nx][ny] != 1 or vis[nx][ny]:
                continue
            vis[nx][ny] = 1
            queue.append([nx, ny])
            area += 1
    return area

cnt = 0
max_area = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] and vis[i][j] == 0:
            res = bfs(i, j)
            if res > max_area:
                max_area = res
            cnt += 1

print(cnt)
print(max_area)
