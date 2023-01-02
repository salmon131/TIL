a=input()
b=input()

'''My Code'''
lst_a = [0]*26 #알파벳 a~z 총 26개. [0]을 총 26개로 초기화
lst_b = [0]*26

for i in a:
    lst_a[ord(i)-97] += 1

for i in b:
    lst_b[ord(i)-97] += 1

for i in range(len(lst_a)):
    if lst_a[i] and lst_b[i]:
        intersection = min(lst_a[i], lst_b[i])    
        lst_a[i] -= intersection
        lst_b[i] -= intersection

print(sum(lst_a) + sum(lst_b))

'''Other Code'''
a = [0]*26
b = a[:]
ans = 0

for i in input(): # 한번에 가능
    a[ord(i)-97] += 1
for i in input():
    b[ord(i)-97] += 1
for i in range(26):
    ans += abs(a[i]-b[i]) # 절댓값 차 이용
print(ans)