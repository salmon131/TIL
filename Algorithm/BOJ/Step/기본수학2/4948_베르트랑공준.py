# 시간초과 코드
def count_prime(num):
    cnt = 0
    for x in range(num+1,2*num+1):
        if x <= 1: 
            continue
        for i in range(2, int(x ** 1/2)+1):
            if x % i == 0: break
        else:
            cnt += 1

    return cnt

# 에라토스의 체를 이용한 코드
def eratos_prime_list(n):
    eratos = [1] * (2 * n + 1)
    eratos[0] = 0
    eratos[1] = 0
    for i in range(2, int(len(eratos) ** 1/2)+1):
        if eratos[i]==1:
            # i의 배수를 모두 제외
            for j in range(i + i, len(eratos), i):
                eratos[j] = 0
    
    return eratos



if __name__=="__main__":
    while True:
        n = int(input())
        if n==0:
            break
        # print(count_prime(n))
        eratos = eratos_prime_list(n)
        print(sum(eratos[n+1:(2*n)+1]))