X = 5
Y = 17
start = [0, 0]
end = [X - 1, Y - 1]

def move(x, y):
    z = [i + j for i, j in zip(x, y)]
    return z

def valid(x):
    if x[0] < end[0] and x[1] < end[1]:
        return True
    return False

roots = [[1, 2], [2, 1], [2, -1], [1, -2]]
cnt = 1

while valid(start):
    if X >= 6:
        cnt = 4
        start = [X - 6, Y]
    for root in roots:
        if valid(move(start, root)):
            start = move(start, root)
            print(start)
            cnt += 1
    print(start)
    break

print(cnt)


