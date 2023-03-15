import sys

"""My Code"""
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

N = A * B * C

# 0부터 9까지의 숫자 카운트를 담을 배열
arr = [0] * 10

for i in str(N):
    arr[int(i)] += 1

print("\n".join(map(str, arr)))


"""Other Code"""
mul = 1
for _ in range(3):
    mul *= int(sys.stdin.readline().strip())

# 계산 결과의 개별 숫자를 리스트로 저장
data = []
while mul:
    data.append(mul % 10)
    mul //= 10

for i in range(10):
    print(data.count(i))
