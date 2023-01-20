import sys

stack = []
answer = 0
k = sys.stdin.readline().strip()
i = 0
while i < len(k):
    if k[i] == '(':
        if k[i+1] == ')': # layser
            answer += len(stack)
            i += 1
        else:
            stack.append(k[i])
    else: 
        stack.pop()
        answer += 1
    i += 1
    
print(answer)