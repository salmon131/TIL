num = int(input())
for i in range(num):
    H, W, N = map(int, input().split())
    floor = N % H
    
    if floor == 0 :
        # 나머지가 0인 경우는 0층이 아니라 꼭대기 층이 되어야한다.
        floor = H     
        room = N // H
    else:
        room = N // H +1

    result = ''
    result += str(floor)
    if room<10:
        result += '0'+str(room)
    else:
        result += str(room)
    
    print(result)
    