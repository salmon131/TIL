import sys
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
arr.reverse()

cnt = 0 
num = arr[0] - 1
for i in arr[1:]:
    if i > num:
        cnt += i - num
    else:
        num = i
    num = num - 1

print(cnt)
