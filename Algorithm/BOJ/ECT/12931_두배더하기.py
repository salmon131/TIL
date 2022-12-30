n = int(input())
arr = list(int(x) for x in input().split())
arr.sort()

cnt = 0

while sum(arr) != 0:
    check = 0
    for i in range(n):
        if arr[i] % 2 != 0 or arr[i] == 0 or arr[i] == 1:
            if arr[i] == 0:
                continue
            else:
                arr[i] -=1
                cnt += 1
            check = 1
    if check == 0:
        for i in range(n):
            arr[i] //= 2
        cnt += 1

print(cnt)