'''my code'''
alphabet = [c for c in range(ord('A'),ord('Z')+1)]

dial_dict = {}

for c in alphabet:
    if c in range(ord('A'), ord('C')+1):
        dial_dict[c] = 2
    elif c in range(ord('D'), ord('F')+1):
        dial_dict[c] = 3
    elif c in range(ord('G'), ord('I')+1):
        dial_dict[c] = 4
    elif c in range(ord('J'), ord('L')+1):
        dial_dict[c] = 5
    elif c in range(ord('M'), ord('O')+1):
        dial_dict[c] = 6
    elif c in range(ord('P'), ord('S')+1):
        dial_dict[c] = 7
    elif c in range(ord('T'), ord('V')+1):
        dial_dict[c] = 8
    else:
        dial_dict[c] = 9


term = input()

time = len(term)
for t in term:
    time += dial_dict[ord(t)]

print(time)

'''develope code'''
alphabet = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
time = 0

term = input()

for i, alpha in enumerate(alphabet):
    number = i+3
    upchar = alpha.upper()
    for j in term:
        if j in upchar:
            time += number

print(time)