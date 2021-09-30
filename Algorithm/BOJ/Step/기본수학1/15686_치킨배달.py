n, m = map(int, input().split())
pizza = n
rest_coupon=0
while (n//m!=0):
    pizza += n//m
    rest_coupon = n%m
    n= n//m+rest_coupon

print(pizza)    