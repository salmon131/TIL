buildings = []
for i in range(int(input())): buildings.append(int(input()))

# 스택, 결과변수
stack = []
result = 0

for b in buildings:
  while stack and stack[-1]<=b:
    stack.pop()
  stack.append(b)

  result += len(stack)-1

print(result)
