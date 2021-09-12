'''my code'''
N = int(input())

if N==1:
    print(1)
    exit()

round_cnt = 1
end = 1

while True:
    if (end + 1 <= N) and (N <= end + 6*round_cnt):
        print(round_cnt+1)
        break
    else:
        end = end + 6*round_cnt
        round_cnt += 1

'''develope code'''
N = int(input())

cell = 1
cnt = 1

while N > cell:
    cell += cnt*6
    cnt += 1
    
print(cnt)