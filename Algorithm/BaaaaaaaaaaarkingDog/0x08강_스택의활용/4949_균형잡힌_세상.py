import sys

while True:
    txt = sys.stdin.readline().rstrip()
    if txt == '.':
        break
    stack = []
    status = 'yes'
    for char in txt:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            pair = '(' if char == ')' else '['
            if stack and stack[-1] == pair:
                stack.pop()
            else:
                status = 'no'
                break
        else:
            continue
    if not stack:
        print(status)
    else:
        print('no')