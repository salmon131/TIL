oasis = [int(input()) for _ in range(int(input()))]

stack = []
result = 0

for o in oasis:
  while stack and stack[-1]<o: # >
    stack.pop()
    result += 1

  stack.append(o)

  if len(stack)>0:
    result += len(stack)-1


print(result)