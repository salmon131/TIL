import sys

n = int(input())
answer = 0

for i in range(n):
    txt = sys.stdin.readline().strip()
    stack = []
    for char in txt:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        answer += 1
        
print(answer)