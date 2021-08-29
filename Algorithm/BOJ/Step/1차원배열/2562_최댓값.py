'''my code'''
import sys

data = []

for i in range(9):
    data.extend(list(map(int,sys.stdin.readline().split())))

print(max(data))
print(data.index(max(data))+1)

'''develope code'''
# 위의 코드는 2차원 배열 생성 시 적합할 것으로 판단
# 1차원 배열에 입력받은 수를 저장할때는 input으로만 사용하는 것이 실행시간이 더 짧을 것?
data = []
for i in range(9):
    data.append(int(input()))

print(max(data))
print(data.index(max(data))+1)