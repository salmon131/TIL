"""
예시 답은 출력되었으나 시간초과로 실패한 답
"""

def list_generator(n):
    n_list = []
    for i in range(1, n+1):
        n_list.append(i)
    return n_list

def find(k, n):
    n_list = list_generator(n)
    for i in range(k-1, 0, -1):
        j = 0
        while True:
            push_list = list_generator(n_list[j])
            n_list[j:j+1] = push_list
            j = j+len(push_list)
            # print(j)
            # print(n_list)
            if j == len(n_list):
                break
    return sum(n_list)

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        k = int(input())
        n = int(input())
        people = find(k, n)
        print(people)

# print(find(2, 3))

# li = [1, 2, 3, 4, 5]
# li[0:1] = [1, 3, 5]
# print(li)




