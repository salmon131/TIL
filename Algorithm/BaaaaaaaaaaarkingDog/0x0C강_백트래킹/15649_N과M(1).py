import sys

N, M = list(map(int, sys.stdin.readline().split()))

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()


