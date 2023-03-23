import sys
from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

N = int(sys.stdin.readline())
queue = deque()
arr = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

def bfs(x, y):
    queue.append([x, y])
    arr[x][y] = 1
    while queue:
        i, j = queue.popleft()
        for dir in range(6):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and not arr[nx][ny]:
                arr[nx][ny] = arr[i][j] + 1
                queue.append([nx, ny])

bfs(r1, c1)

print(arr[r2][c2] - 1)