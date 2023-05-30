import sys
from collections import deque

def bfs(start, end):
    q = deque()
    q.append(start)
    sx, sy, sz = start
    visit[sz][sy][sx] = 0
    while q:
        nowx, nowy, nowz = q.popleft()
        if nowx == end[0] and nowy == end[1] and nowz == end[2]:
            return visit[nowz][nowy][nowx]
        for i, j, k in zip(dx, dy, dz):
            nx = i + nowx
            ny = j + nowy
            nz = k + nowz

            if nx < 0 or nx >=x or ny < 0 or ny >= y or nz <0 or nz >= z:
                continue
            if board[nz][ny][nx] == 1 and visit[nz][ny][nx] == -1:
                visit[nz][ny][nx] = visit[nowz][nowy][nowx]+1
                q.append([nx, ny, nz])
    return -1

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while True:
    z, y, x = map(int, sys.stdin.readline().split())
    if x+y+z == 0:
        break
    board = [[[] * (x) for _ in range(y)] for _ in range(z)]
    visit = [[[-1] * (x) for _ in range(y)] for _ in range(z)]
    start = []
    end = []
    for i in range(z):
        for j in range(y):
            tmp = input()
            for idx, item in enumerate(tmp):
                if item == '.' or item == 'S' or item == 'E':
                    if item == 'S':
                        start = [idx, j, i]
                    elif item == 'E':
                        end = [idx, j, i]
                    board[i][j].append(1)
                else:
                    board[i][j].append(0)
        input()
    ans = bfs(start, end)
    if ans == -1:
        print('Trapped!')
    else:
        print('Escaped in', ans, 'minute(s).')