import sys

'''my code'''
N, L = map(int, sys.stdin.readline().split())
leaks = map(int, sys.stdin.readline().split())
leaks = sorted(leaks)

tape_cnt = 1
tape_start = leaks[0] - 0.5
tape_end = tape_start + L

for i, x in enumerate(leaks):
    if x + 0.5 > tape_end:
        tape_cnt += 1
        tape_start = x - 0.5
        tape_end = tape_start + L

print(tape_cnt)

'''short code example'''
I= lambda:map(int,input().split()) # 입력 함수는 한번만 생성하여 중복 제거
N,L=I()
A=sorted(I()) # sorted를 바깥에 씀으로써 2줄을 1줄로
R=l=0 # ?? 이런게 되는구나
for a in A:
    if a > l:
        R += 1
    l = L -1 + a
print(R)