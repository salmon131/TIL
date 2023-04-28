import sys

N = int(sys.stdin.readline())

# 자리 정보
seat = [[0]*(N+1) for _ in range(N+1)]

# 좋아하는 학생 정보
like = []
# 학생 번호별 좋아하는 학생 정보
input_info = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N ** 2):

    input = list(map(int, sys.stdin.readline().split()))
    input_info.append(input)
    now = input[0]
    like = input[1:]

    result = []

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not seat[i][j]:
                like_count = 0
                empty_count = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 1 <= nx < N + 1 and 1 <= ny < N + 1:
                        if seat[nx][ny] in like:
                            like_count += 1

                        if not seat[nx][ny]:
                            empty_count += 1

                result.append((like_count, empty_count, i, j))

    result = sorted(result, key = lambda x: (-x[0], -x[1], x[2], x[3]))

    seat[result[0][2]][result[0][3]] = now

input_info.sort()

sum = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):

        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            # 교실 내에 있는지
            if (1 <= nx < N + 1 and 1 <= ny < N + 1):
                if (seat[nx][ny] in input_info[seat[i][j]-1]):
                    count += 1

        # 인접한 칸에 좋아하는 학생이 있을 경우
        if (count != 0):
            sum += 10**(count-1)

print(sum)