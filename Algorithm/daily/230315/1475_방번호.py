import sys

N = sys.stdin.readline().strip()
arr = [0] * 10

for i in N:
    num = int(i)
    if num == 6 or num == 9:
        if arr[6] < arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[num] += 1

print(max(arr))
