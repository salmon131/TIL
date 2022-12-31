N = input()
lst = [0]*26 #알파벳 a~z 총 26개. [0]을 총 26개로 초기화

for i in N:
    lst[ord(i)-97] += 1
    
for i in lst:
    print(i, end=' ')
 