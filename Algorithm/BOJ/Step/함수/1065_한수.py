'''my code'''
# (진행 중)

def hansoo_checker(num: str):
    """
    parmam : string type number
    return : boolean
    """
    # 첫째 자리 수는 다음 자리가 없으므로 비교할 수를 0으로 초기화
    pre = int(num[0])
    for idx in range(1, len(num)):
        nex = int(num[idx])

        # 등차 초기화
        if idx == 1:
            diff = abs(pre-nex)
        
        if diff != abs(pre-nex) : return 0

        # 자리수 하나 오른쪽 이동
        pre = nex

    # 모든 자리 체크가 완료
    return 1

def count_hansoo(N: str):
    """
    parmam : string type number
    return : number of hansoo smaller than N
    """
    count = 0
    for num in range(1,int(N)+1): 
        if hansoo_checker(str(num)): count+=1
    
    return count

N = input()
print(hansoo_checker('11'))
# print(count_hansoo(N))
