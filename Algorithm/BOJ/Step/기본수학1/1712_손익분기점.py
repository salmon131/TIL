A, B, C = map(int, input().split())

if C-B <=0 :
    print(-1)
else:
    break_end_point = A//(C-B)

    if break_end_point>=0:
        print(break_end_point+1)
    else:
        print(-1)