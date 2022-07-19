import sys
Y, X = map(int, sys.stdin.readline().split())
start = [0, 0]
end = [X - 1, Y - 1]

roots = [[1, 2], [2, 1], [2, -1], [1, -2]]
used = []
cnt = 1

def move(x, y):
    z = [i + j for i, j in zip(x, y)]
    return z

def valid(x):
    if x[1] >= 0:
        if x[0] <= end[0] and x[1] <= end[1]:
            return True
    return False

if end[0] >= 6:
    cnt += 4
    start = [6, 0]

stop = False
while not stop:
    for i, root in enumerate(roots):
        if valid(move(start, root)):
            start = move(start, root)
            used.append(tuple(root))
            cnt += 1
            break
        if i == 3:
            stop = True

if cnt == 5 and len(set(used)) == 1:
    print(cnt - 1)
else:
    print(cnt)