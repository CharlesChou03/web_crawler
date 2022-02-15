# feature
# 1. input vocabulary and save by file.
#   1.1. check vocabulary validation.
#   1.2. show existing message if vocabulary already exist.
#   1.3. validate input (vocabulary only).
# 2. display n vocabulary randomly.
#   2.1. get vocabulary explanation from online dictionary, ex: https://www.ldoceonline.com/dictionary/{vocabulary}.
#   2.2. display information about total vocabulary number so far.
#   2.3. default number is 3
#   2.4. validate input (number only).


# test case
# [create_vocabulary.py]
# 1. vocabulary file is not exist. -> result: create file and write vocabulary to the vocabulary.txt.
# 2. vocabulary file is exist.
#   2.1. input new vocabulary. -> result: append new vocabulary to the file.
#   2.2. input exist vocabulary. -> result: display exist message and exit.
#   2.3. validate input. -> result: display validation message if invalid input and exit.

# [display_vocabulary.py]
# 1. display n vocabulary randomly.
# 2. validate input