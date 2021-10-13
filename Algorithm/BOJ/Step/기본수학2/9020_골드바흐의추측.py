
from typing import List

# 에라토스의 체를 이용한 소수 찾기
def eratos_prime_list(n):
    eratos = [1] * n
    eratos[0] = 0
    eratos[1] = 0
    for i in range(2, int(len(eratos) ** 1/2)+1):
        if eratos[i]==1:
            # i의 배수를 모두 제외
            for j in range(i + i, len(eratos), i):
                eratos[j] = 0
    
    return eratos

def goldbach_partition(n):
    # n-2까지의 소수의 set을 생성
    eratos = eratos_prime_list(n-2)
    prime_list = [i for i in range(len(eratos)) if eratos[i]==1]

    min_diff = 9999
    gold_set : List
    for prime in prime_list:
        if prime > n//2:
            break
        a = prime
        b = n - a
        if b in prime_list:
            i = prime_list.index(a)
            j = prime_list.index(b)
            diff = abs(i-j)
            if diff < min_diff:
                min_diff = diff
                gold_set = [i, j]

    return prime_list[gold_set[0]], prime_list[gold_set[1]]


n = int(input())
for i in range(n):
    num = int(input())
    part1, part2 = goldbach_partition(num)
    print(f"{part1} {part2}")
