import random
import os

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

print("Please input destination (n or r): ", end='')
destination = input()
if destination == "n":
    FILE_PATH = "./vocabulary.txt"
elif destination == "r":
    FILE_PATH = "./review_vocabulary.txt"
else:
    print("Please input valid destination! (n for normal or r for review)")
    exit(0)
print("Execute file path is \"%s\" by destination \"%s\"" % (FILE_PATH, destination))

if not os.path.isfile(FILE_PATH):
    print("Please create \"vocabulary.txt\" first!")
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

picked_n = len(items)
print("Today vocabulary (%s/%s)" % (picked_n, count))
for v in items:
    print("-> " + v)
