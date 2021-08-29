'''my code'''
N = int(input())
for i in range(N):
    scores = list(map(int, input().split()))

    # 첫 수는 학생 수이며 따로 저장 후 list에서 삭제
    n = scores[0] 
    del scores[0]

    # 평균 계산
    sum = 0
    for s in scores:
        sum+=s
    average = sum/n

    # 평균을 넘는 학생 수 구하기
    cnt = 0
    for s in scores:
        if s>average: cnt+=1

    print("{:.3f}%".format(cnt/n*100))





