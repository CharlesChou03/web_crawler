import requests
from bs4 import BeautifulSoup
import os

NOT_FOUND_MESSAGE = "Did you mean:"

print("Please input vocabulary: ", end='')
vocabulary = input()
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
# https://blog.csdn.net/Max_R/article/details/30219035
if not vocabulary.encode( 'UTF-8' ).isalpha():
    print("Please input valid vocabulary!")
    exit(0)
vocabulary = vocabulary.lower()

url = "https://www.ldoceonline.com/dictionary/" + vocabulary
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
response = requests.get(
    url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("h1")
if result.getText() == NOT_FOUND_MESSAGE:
    print("The \"%s\" is not found, please check it again!" % vocabulary)
    exit(0)

count = 0
exist_vocabulary = set()
# https://www.runoob.com/python/python-func-open.html
if os.path.isfile(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        for line in f:
            count = count + 1
            line_lower = line.lower()
            exist_vocabulary.add(line_lower.rstrip())
        f.close()
with open(FILE_PATH, "a+") as f:
    if not vocabulary in exist_vocabulary:
        f.write(vocabulary + "\n")
        print("The \"%s\" is successful appended!" % vocabulary)
    else:
        print("The \"%s\" is already exist!" % vocabulary)
    f.close()