'''my code'''
# (진행 중)

def hansoo_checker(num: str):
    """
    parmam : string type number
    return : boolean
    """
    # 첫째 자리 수를 pre로 초기화
    pre = int(num[0])
    # 둘째 자리 수를 nex로 설정하고 반복시작
    for idx in range(1, len(num)):
        nex = int(num[idx])

        # 첫 수행시 등차 초기화 
        if idx == 1:
            diff = pre-nex
        
        if diff != (pre-nex) : return 0

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

if __name__=="__main__":
    N = input()
    print(count_hansoo(N))
