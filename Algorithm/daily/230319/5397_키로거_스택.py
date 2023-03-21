import sys

N = int(sys.stdin.readline())
for _ in range(N):
    typing = sys.stdin.readline().strip()
    left, right = [], []
    for typ in typing:
        if typ == '<':
            if left:
                right.append(left.pop())
        elif typ == '>':
            if right:
                left.append(right.pop())
        elif typ == '-':
            if left:
                left.pop()
        else:
            left.append(typ)
    left.extend(reversed(right))
    print(''.join(left))
