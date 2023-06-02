import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp_up = [[-1e9] * M for _ in range(N)]
dp_down = [[-1e9] * M for _ in range(N)]

# 시작점과 끝점 설정
dp_up[N-1][0] = board[N-1][0]
dp_down[N-1][M-1] = board[N-1][M-1]

# 상승 점수 채우기
for i in range(N-1, -1, -1):
    for j in range(M):
        # 시작점이면 패스
        if i == N - 1 and j == 0:
            continue
        # 아래에서 올라올 수 있는 경우
        # 현재 칸 상승점수와 아래 칸 상승점수 비교하여 큰 값으로 대체
        if i < N - 1:
            dp_up[i][j] = max(dp_up[i][j], dp_up[i + 1][j])
        
        # 왼쪽에서 올 수 있는 경우
        # 현재 칸 상승점수와 왼쪽 칸 상승점수 비교하여 큰 값으로 대체
        if j > 0:
            dp_up[i][j] = max(dp_up[i][j], dp_up[i][j - 1])

        # 현재 칸 값을 더해주어 업데이트
        dp_up[i][j] += board[i][j]

# 하강 점수 채우기
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        # 도착점이면 패스
        if i == N - 1 and j == M - 1:
            continue
        # 아래에서 올라올 수 있는 경우
        # 현재 칸 하강점수와 아래 칸 하강점수 비교하여 큰 값으로 대체
        if i < N - 1:
            dp_down[i][j] = max(dp_down[i][j], dp_down[i + 1][j])

        # 오른쪽에서 올 수 있는 경우
        # 현재 칸 하강점수와 오른쪽 칸 하강점수 비교하여 큰 값으로 대체
        if j < M - 1:
            dp_down[i][j] = max(dp_down[i][j], dp_down[i][j+1])
        
        # 현재 칸 값을 더해주어 업데이트
        dp_down[i][j] += board[i][j]

result = -1e9
for i in range(N):
    for j in range(M):
        result = max(result, dp_up[i][j] + dp_down[i][j])

print(result)