num = int(input())
for i in range(num):
    x, y = map(int, input().split())

    k = 1
    while True:
        x = x + k
        k+=1
        if x >= y-1:
            break
        
    
    print(k)

