import sys

def draw_stars(n):
    if n==3:
        return ['***', '* *', '***']
    stars = draw_stars(n//3)
    arr = []
    for s in stars:
        arr.append(s*3)
    for s in stars:
        arr.append(s+' '*(n//3)+s)
    for s in stars:
        arr.append(s*3)
    return arr

N = int(sys.stdin.readline().strip())
print(*draw_stars(N), sep='\n')