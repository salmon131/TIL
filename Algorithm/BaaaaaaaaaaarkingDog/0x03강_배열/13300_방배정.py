import sys
import math

'''My code
1. 남학생 여학생 배열을 학년 수 만큼 생성
2. 각 학년 인덱스에 대해 인원 저장
3. 두 배열을 합쳐 loop돌며 K로 나누어 떨어지면 몫 만큼, 나머지가 있을경우 몫 + 1 만큼 방 수 증가

'''
N, K = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

boys = [0] * 6
girls = [0] * 6
room = 0

for gender, grade in arr:
    if gender == 0:
        girls[grade-1] += 1
    else:
        boys[grade-1] += 1

for i in boys + girls:
    if i:
        room += math.ceil(i/K)
        
print(room)