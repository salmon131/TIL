from itertools import groupby

N = int(input())
count = 0

for i in range(N):
    word = input()

    group = groupby(word)
    keys = [key for key, items in group]
    if len(keys)==len(set(keys)):
        count += 1

print(count)