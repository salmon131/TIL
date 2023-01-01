"""
1. 두 수의 합이 x보다 큰 경우 - 더 작은 값을 더해야하므로 right-1
2. 두 수의 합이 x보다 작은 경우 - 더 큰 값을 더해야하므로 left+1
3. 두 수의 합이 x인 경우 - answer+1 & left+1
"""

import sys
n = int(input())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

answer = 0
left, right = 0, n-1 # 왼쪽, 오른쪽
while left < right:
    temp = numbers[left] + numbers[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)