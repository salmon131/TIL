
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
    # n까지의 소수의 set을 생성
    eratos = eratos_prime_list(n)
    a, b = n//2, n//2
    while True:
        # 둘 다 소수면 return
        if eratos[a]==1 and eratos[b]==1:
            return a, b
        else:
            a -= 1
            b += 1

n = int(input())
for i in range(n):
    num = int(input())
    part1, part2 = goldbach_partition(num)
    print(f"{part1} {part2}")
