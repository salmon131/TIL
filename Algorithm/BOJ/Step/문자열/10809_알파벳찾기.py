import re

word = input()

alphabet = [chr(c) for c in range(ord('a'),ord('z')+1)]
result = []

for w in alphabet:
    match_char = re.search(w, word)
    if match_char is None:
        result.append("-1")
    else:
        result.append(str(match_char.start()))

print(' '.join(map(str, result)))
