n = int(input())
stk = []
for i in range(n):
    num = int(input())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)
print(sum(stk))