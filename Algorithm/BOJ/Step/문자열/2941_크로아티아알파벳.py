'''my code'''
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

term = input()
for c in croatia:
    while c in term:
        term = term.replace(c, "0")

print(len(term))

'''develope code 1'''
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

term = input()
num=0
for c in croatia:
    if c in term:
        num += term.count(c)
        term = term.replace(c,"")

print(len(term)+num)


'''develope code 2'''
term = input()
print(len(term)-sum(map(term.count,['-','=','lj','nj','dz='])))