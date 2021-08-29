'''my code'''
N = int(input())
data = []
data = list(map(int, input().split()))

score_sum = 0
m = max(data)
for score in data:
    score_sum += score/m*100

print(score_sum/len(data))
