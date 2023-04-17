import sys

def draw_stars(n):
    if n==2:
        return ['  *  ', ' * * ', '*****']
    stars = draw_stars(n//2)
    arr = []
    for s in stars:
        arr.append(' '*(len(stars))+s+' '*(len(stars)))
    for s in stars:
        arr.append(s+' '+s)
    return arr

N = int(sys.stdin.readline().strip())
print(*draw_stars(N//3), sep='\n')