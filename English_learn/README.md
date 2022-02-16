# feature
## 1. input vocabulary and save by file.
* check vocabulary validation
* show existing message if vocabulary already exist.
* validate input (vocabulary only).
## 2. display n vocabulary randomly.
* get vocabulary explanation from online dictionary, ex: https://www.ldoceonline.com/dictionary/{vocabulary}.
* display information about total vocabulary number so far.
* default number is 3
* validate input (number only).
* display error message if display vocabulary without creating vocabulary file.
* display proportion (picked/total).


# test case
## [create_vocabulary.py]
## 1. vocabulary file is not exist.
* input new vocabulary. -> create file and write vocabulary to the vocabulary.txt.
## 2. vocabulary file is exist.
* input new vocabulary. -> result: append new vocabulary to the file.
* input exist vocabulary. -> result: display exist message and exit.
* validate input. -> result: display validation message if invalid input and exit.

## [display_vocabulary.py]
## 1. display n vocabulary randomly.
## 2. validate input
* validate input. -> result: display validation message if invalid input and exit.


# you can learn vocabulary from here
* https://www.ldoceonline.com/
