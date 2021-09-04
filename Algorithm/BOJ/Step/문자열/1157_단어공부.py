# to lower case
word = input().lower()

alphabet = [chr(c) for c in range(ord('a'),ord('z')+1)]
word_count= [word.count(alpha) for alpha in alphabet]

# if there is duplicate max value
if word_count.count(max(word_count))>1:
    print("?")
else:
    print(alphabet[word_count.index(max(word_count))].upper())

