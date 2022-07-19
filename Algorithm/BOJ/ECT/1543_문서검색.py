import sys

document = sys.stdin.readline().strip()
search = sys.stdin.readline().strip()

'''my code'''
i = 0
cnt = 0

while i < len(document):
    if document[i:i+len(search)] == search:
        i += len(search)-1
        cnt += 1
    i += 1
    
print(cnt)

'''develope code 1'''
print(document.count(search))