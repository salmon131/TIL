import sys

queue = []
arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

row, col = map(int, sys.stdin.readline().split())
vis = [[0 for _ in range(col)] for _ in range(row)] # 방문 정보
for _ in range(row):
    arr.append(list(map(int, sys.stdin.readline().split())))

def bfs(i, j):
    if vis[i][j] == 1:
        return 0
    area = 1
    vis[i][j] = 1 # 방문 표시
    queue.insert(0, [i, j])
    while queue:
        i, j = queue.pop()
        for dir in range(4): # 상하좌우 탐색
            nx = i + dx[dir]
            ny = j + dy[dir]
            if nx < 0 or nx >= row or ny < 0 or ny >= col: # 배열 범위 벗어나는지 확인
                continue
            if arr[nx][ny] != 1 or vis[nx][ny]: # 값이 1아니거나 이미 방문했는지 확인
                continue
            vis[nx][ny] = 1
            queue.insert(0, [nx, ny])
            area += 1
    return area

areas = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]:
            areas.append(bfs(i, j))
cnt = len([i for i in areas if i])
if cnt:
    print(cnt)
    print(max(areas))
else:
    print(cnt)
    print(0)

