import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(R)]
f_queue, j_queue = deque([]), deque([])
f_visited, j_visited = [[-1] * C for _ in range(R)], [[-1] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == "J":
            j_queue.append([i, j])
            j_visited[i][j] = 0
        if arr[i][j] == "F":
            f_queue.append([i, j])
            f_visited[i][j] = 0


def bfs():
    while f_queue:
        x, y = f_queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C:
                if f_visited[nx][ny] == -1 and arr[nx][ny] != "#":  # 아직 방문하지 않았고 벽이 아니면
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append([nx, ny])

    while j_queue:
        x, y = j_queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C:
                if j_visited[nx][ny] == -1 and arr[nx][ny] != "#":  # 아직 방문하지 않았고 벽이 아니면
                    if (
                        f_visited[nx][ny] == -1 or 
                        j_visited[x][y] + 1 < f_visited[nx][ny]
                    ):  # 불이 오지 않았거나 불보다 앞질러있으면
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append([nx, ny])
            else:  # 범위를 벗어난 것이 큐에 있었다면 탈출 조건에 해당
                return j_visited[x][y] + 1

    return "IMPOSSIBLE"


print(bfs())
