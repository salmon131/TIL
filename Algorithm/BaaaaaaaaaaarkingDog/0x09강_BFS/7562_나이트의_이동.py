from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs(x, y, x_end, y_end):
    q = deque()
    q.append([x, y])
    array[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == x_end and y == y_end:
            return array[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length:
                if array[nx][ny] == 0:
                    q.append([nx, ny])
                    array[nx][ny] = array[x][y] + 1


tc = int(input())
while tc:
    length = int(input())
    array = [[0] * length for _ in range(length)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
        tc -= 1
        continue
    ans = bfs(x1, y1, x2, y2)
    print(ans)
    tc -= 1
