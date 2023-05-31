import sys
import copy

N, M = map(int, sys.stdin.readline().split())
cctv = [] # cctv의 종류와 좌표 넣기
graph = [] # 주어진 데이터 넣기

mode = [
    [], # cctv를 1번부터 시작하도록
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    for j in range(M):
        if row[j] in range(1, 6):
            cctv.append([row[j], i, j])


def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            if board[nx][ny] == 6:
                break 
            elif board[nx][ny] == 0:
                board[nx][ny] = 7 # cctv가 감시하는 곳일 경우 7로 채우기

def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += arr[i].count(0) # 사각지대 카운트
        min_value = min(min_value, cnt)
        return
    
    tmp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(tmp, i, x, y) # cctv 번호의 가능한 경우로 채우기
        dfs(depth + 1, tmp)
        tmp = copy.deepcopy(arr)

min_value = int(1e9)
dfs(0, graph)
print(min_value)