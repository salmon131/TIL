import sys
N = int(input())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

print(numbers.count(x))