import sys

def cantor(length):
    global answer
    if length == 3:
        answer += '- -' 
        return
    cantor(length // 3)
    for _ in range(length // 3):
        answer += ' '
    cantor(length // 3)

while True:
    try:
        N = sys.stdin.readline().strip()
        if N == '':
            break
        answer = ''
        length = 3 ** int(N)
        if length == 1:
            print('-')
            continue
        cantor(length)
        print(answer)
    except EOFError:
        break