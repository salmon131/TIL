N = int(input())

def find_turn_number(N):
    turn = 2
    end = 1
    if N == 1:
        return 1, 1
    while True:
        start = end+1
        end = end + turn
        if start <= N and N <= end :
            return turn, start
        turn+=1

def find_bunsu(N, turn, start):
    # even
    if turn%2==0:
        bunja = N-start+1
    else:
        bunja = turn-(N-start)

    bunmo = turn-bunja+1
    bunsu = f"{bunja}/{bunmo}"

    return bunsu

turn, start = find_turn_number(N)
bunsu = find_bunsu(N, turn, start)

print(bunsu)





