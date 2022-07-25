import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()

    que = 0
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            if not que: # 큐에 아무것도 없으면 비교 기준 지정
                a = A[i]
                b = B[i]
                que += 1
            elif a == B[i] and b == A[i]: # 말 위치 바꿔서 일치하면 카운트 +1
                cnt += 1
                que -= 1
            else: # 말 위치 못바꾸면 큐 +1
                a = A[i]
                b = B[i]
                que += 1

    # 큐에 남은 수만큼 말 뒤집어야함
    print(que + cnt)

