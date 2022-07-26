import sys

T = int(sys.stdin.readline())
arrs = []
for _ in range(T):
    arrs.append(list(map(int, sys.stdin.readline().strip().split())))

arrs.sort(key=lambda x:x[0]) # 도착시간 짧은 순으로 정렬

prev_cow_end = arrs[0][0] + arrs[0][1] # 첫 번째 소 검문종료 시각
for i, cow in enumerate(arrs[1:], start=1): # 두 번째 소부터 검사
    curr_cow_start = cow[0] # 시작 시각
    curr_cow_latency = cow[1] # 검문 시간
    if prev_cow_end > curr_cow_start: # 현재 소 도착 시간이 앞의 소 끝나는 시간보다 먼저라면
        prev_cow_end = prev_cow_end + curr_cow_latency # 앞의 소 끝날때 까지 기다려야함
    else:
        prev_cow_end = curr_cow_start + curr_cow_latency # 그게 아니면 도착시간에 맞춰 검문

print(prev_cow_end)
