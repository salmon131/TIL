import sys
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

arr.sort(reverse=True)

sum = 0
for idx, price in enumerate(arr, start=1):
    if idx % 3:
        sum += price
print(sum)