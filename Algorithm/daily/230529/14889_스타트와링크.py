import sys

N = int(sys.stdin.readline().strip())

visited = [0] * N
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_diff = int(1e9)


def dfs(depth, idx):
    global min_diff
    if depth == N//2:
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    power1 += arr[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += arr[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(min_diff)