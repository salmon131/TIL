'''my code'''
from itertools import groupby

N = int(input())
for i in range(N):
    result = input()
    count = [] # 연속된 정답 개수를 저장할 list
    for k, g in groupby(result):
        if k == 'O':
            count.append(len(list(g)))

    # count 속 원소를 토대로 누적 점수 계산
    ssum = 0
    for c in count:
        sum = 0
        for i in range(c, 0, -1):
            sum+=i
        ssum+=sum
    print(ssum)







