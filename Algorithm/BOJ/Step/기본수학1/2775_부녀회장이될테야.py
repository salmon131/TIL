# T = int(input())
# for i in range(T):
#     k = int(input())
#     n = int(input())
#     people = find(k, n)
#     print(people)

# def find(k, n):
#     sum_num = k-1

def acc_sum(a):
    if a<=1:
        return 1
    return a + acc_sum(a-1)

# print(acc_sum(T))

# k층 n호
def nested(k, n):
    sum=0
    if k<=1:
        sum += acc_sum(n)
        return sum
    return sum + nested(k-1, n)


print(nested(2, 2))