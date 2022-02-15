import random

FILE_PATH = "./vocabulary.txt"
DEFAULT_N = 3

print("Please input vocabulary number you wanna see: ", end='')
inp = input()

if not inp.encode( 'UTF-8' ).isdigit():
    print("Please input digit!")
    exit(0)

if not inp:
    n = DEFAULT_N
else:
    n = int(inp)
print(n)
exit(0)
exist_vocabulary = set()
count = 0
with open(FILE_PATH, "r") as f:
    for line in f:
        count = count + 1
        line_lower = line.lower()
        exist_vocabulary.add(line_lower.rstrip())
    f.close()

if count < n:
    n = count

items = []
for i in range(n):
    item = random.choices(list(exist_vocabulary))
    exist_vocabulary.remove(item[0])
    items.append(item[0])

print("Today vocabulary")
for v in items:
    print("-> " + v)
