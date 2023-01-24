import sys

queue = [[0, 0]]
arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
vis = [[0 for _ in range(M)] for _ in range(N)] # 방문 정보
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

while queue:
    i, j = queue.pop()
    vis[i][j] = 1 # 방문 표시
    for dir in range(4): # 상하좌우 탐색
        nx = i + dx[dir]
        ny = j + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: # 배열 범위 벗어나는지 확인
                continue
        if not arr[nx][ny] or vis[nx][ny]: # 이미 방문했는지 확인
            continue
        vis[nx][ny] = 1
        arr[nx][ny] = arr[i][j] + 1
        queue.insert(0, [nx, ny])

print(arr[N-1][M-1])