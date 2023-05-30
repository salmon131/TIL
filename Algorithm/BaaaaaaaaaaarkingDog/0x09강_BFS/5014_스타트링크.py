from collections import deque
import sys

f, s, g, u, d = map(int, sys.stdin.readline().split())


def bfs(start, goal):
    q = deque()
    visited = [-1] * (f + 1)

    q.append(start)
    visited[start] = 0

    while q:
        x = q.popleft()

        if x == goal:
            return visited[x]

        for nx in (x + u, x - d):
            if 0 < nx <= f and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1

    return "use the stairs"


print(bfs(s, g))
