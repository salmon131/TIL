"""
< 접근법 >

- 원형 연결리스트 자료구조가 아닌 배열로 풀어볼 수 있다.
- 숫자를 담는 배열은 만들지 않아도 된다.
- prev, next 를 저장하는 배열 두개만 필요하다.
- prev와 next의 첫번째와 마지막 값을 주의해서 넣어준다.
"""

import sys

N, K = map(int, sys.stdin.readline().strip().split())
pre = [0 for _ in range(5001)]
nxt = [0 for _ in range(5001)]

for i in range(1, N + 1):
    pre[i] = N if i == 1 else i - 1
    nxt[i] = 1 if i == N else i + 1

cur = 1 # 현재 위치
cnt = 1 # 현재 움직인 갯수
len = N
ans = []

while len:
    if cnt == K:
        nxt[pre[cur]] = nxt[cur]
        pre[nxt[cur]] = pre[cur] 
        ans.append(cur)
        cnt = 1
        len -= 1
    else:
        cnt += 1
    cur = nxt[cur] # 다음 위치로 이동

print('<' + ', '.join(map(str, ans)) + '>')