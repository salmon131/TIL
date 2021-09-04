'''my code'''

# 각 자리수의 합을 반환하는함수
def d(n):
    sum = 0
    while(n!=0):
        sum += n%10
        n = n//10
    return sum

def self_num_ver1():
    data = []
    n = 1
    dn = 1
    while(n<=10000): # n이 증가할 때 dn이 증가한다는 보장이 없기 때문
        dn = n + d(n)
        data.append(dn)
        n += 1

    data.sort()
    for i in range(1, 10001):
        if i not in data:
            print(i)

'''develope code'''
def self_num_ver2():
    numbers = set(range(1, 10000))
    remove_set = set()  # 생성자가 있는 숫자 set
    for num in numbers :
        for n in str(num):
            num += int(n)
        remove_set.add(num)  # add: 집합에 요소를 추가할 때

    self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
    for self_num in sorted(self_numbers):  # sorted 함수로 정렬
        print(self_num)

if __name__=="__main__":
    self_num_ver2()