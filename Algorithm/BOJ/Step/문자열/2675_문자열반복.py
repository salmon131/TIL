case_num = int(input())
for num in range(case_num):
    repeat_num, string = map(str, input().split())

    result = ''
    for char in string:
        result=''.join([result, char*int(repeat_num)])

    print(result)
