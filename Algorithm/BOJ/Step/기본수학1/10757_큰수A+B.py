"""
method 1
"""
A, B = map(int, input().split())
print(A+B)

"""
method 2
"""
A , B = input().split()
large = A[::-1] if len(A)>len(B) else B[::-1]
small = B[::-1] if len(A)>len(B) else A[::-1]

carry = 0
result = ''

for i in range(len(small)):
    sum = int(large[i]) + int(small[i]) + carry
    carry = 1 if sum >= 10 else 0

    result = str(sum % 10) + result

# 남은 자리수 처리
if carry==1 and len(A)==len(B):
    result = "1" + result
else:
    for j in range(i+1, len(large)):
        result = str(int(large[j]) + carry) + result
        carry = 0

print(result)

