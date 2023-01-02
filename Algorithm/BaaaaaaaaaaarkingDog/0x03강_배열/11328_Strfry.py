import sys

N = int(input())

for _ in range(N):
    a, b = sys.stdin.readline().strip().split()
    if sorted(a) == sorted(b):
        print("Possible")
    else:
        print("Impossible")