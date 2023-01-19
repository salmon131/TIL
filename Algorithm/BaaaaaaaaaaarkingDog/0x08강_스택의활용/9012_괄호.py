import sys

n = int(input())

for _ in range(n):
    txt = sys.stdin.readline().rstrip()
    stack = []
    status = 'YES'
    for char in txt:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            pair = '(' if char == ')' else '['
            if stack and stack[-1] == pair:
                stack.pop()
            else:
                status = 'NO'
                break
        else:
            continue
    if not stack:
        print(status)
    else:
        print('NO')