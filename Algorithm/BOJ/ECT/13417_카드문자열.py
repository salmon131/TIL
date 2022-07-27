import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = sys.stdin.readline().strip().split()

    result = cards[0]
    for card in cards[1:]:
        if card <= result[0]: # 맨 앞 글자보다 사전순 같거나 빠르면 맨 왼쪽으로
            result = card + result
        else:
            result = result + card

    print(result)

