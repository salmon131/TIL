'''my code'''
mul = 1
for i in range(3):
    mul *= int(input())

# 계산 결과의 개별 숫자를 리스트로 저장
data = []
while(mul!=0):
    data.append(mul%10)
    mul = mul//10

# 첫 줄부터 해당 줄의 숫자가 몇 번 쓰였는지 출력
for i in range(10):
    print(data.count(i))