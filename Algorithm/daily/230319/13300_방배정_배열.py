import sys

N, K = map(int, sys.stdin.readline().split())
boys = [0] * 6
girls = [0] * 6
room = 0

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    if S: # 남학생
        boys[Y-1] += 1
    else: # 여학생
        girls[Y-1] += 1

for i in boys + girls:
    room += i // K
    if i % K:
        room += 1

print(room)