
while True: 
    len_list = list(map(int, input().split()))
    if len_list == [0, 0, 0]:
        break
    max_len = max(len_list)
    len_list.remove(max_len)
    
    squared_sum = 0
    for line in len_list:
        squared_sum += line**2
    
    if squared_sum == max_len**2:
        print("right")
    else:
        print("wrong")
