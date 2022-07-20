import sys
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

arr.sort(reverse=True)

sum = 0
for rank, tip in enumerate(arr):
    if tip > rank:
        sum += tip - rank

print(sum)