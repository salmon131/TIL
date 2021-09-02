import re

word = input()

alphabet = [chr(c) for c in range(ord('A'),ord('X'))]

for w in alphabet:
    match_char = re.search(w, word)
    if match_char is None:
        print("-1 ")
    else:
        print(f"{match_char.start()} ")
