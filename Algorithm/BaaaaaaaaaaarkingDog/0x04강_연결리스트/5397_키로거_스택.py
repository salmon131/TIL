'''
- 문자열을 그대로 두고 커서를 움직이는 것 -> 일반적 생각 -> 시간 복잡도 높음 -> 해결 안됨
- 발상의 전환 필요 -> 커서를 그대로 두고 문자열을 움직이는 것
- 커서의 왼쪽과 오른쪽 부분을 두 개의 스택으로 나눠서 생각
'''
import sys

N = int(sys.stdin.readline())
for _ in range(N):
    inputs = sys.stdin.readline().strip()
    left, right = [], []
    for typ in inputs:
        if typ == '<':
            if left:
                right.append(left.pop())
        elif typ == '>':
            if right:
                left.append(right.pop())
        elif typ == '-':
            if left:
                left.pop()
        else: # 그냥 문자 입력 들어왔을 경우
            left.append(typ)
    left = left.extend(reversed(right))
    print(''.join(left))