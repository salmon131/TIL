import sys

k = sys.stdin.readline().strip()

stack = []
answer = 0
tmp = 1

for i in range(len(k)):
    if k[i] == '(':
        stack.append(k[i])
        tmp *= 2
    elif k[i] == '[':
        stack.append(k[i])
        tmp *= 3
    elif k[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if k[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else: # k[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if k[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3
        
if stack:
    print(0)
else:
    print(answer)