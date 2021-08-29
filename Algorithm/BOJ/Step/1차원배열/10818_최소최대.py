'''my code'''
N = int(input())
data= list(map(int, input().split()))
data.sort()
print("{} {}".format(data[0], data[-1]))

'''develope code'''
N = int(input())
data= list(map(int, input().split()))
# list의 min, max내장함수 사용
print(min(data), max(data))