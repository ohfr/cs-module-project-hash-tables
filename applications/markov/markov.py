import random
from os import path
import re

words = ''
# Read in all the words in one go
with open(path.abspath("applications/markov/input.txt")) as f:
    words = f.read()


# TODO: analyze which words can follow other words
# Your code here

# words = re.sub(r"[^\w\s']+", '', words) for only words and no special chars

words = re.sub(r"(\r\n|\r|\n|\t)", ' ', words)

lookup = {}

wordArr = words.split(' ')


for i in range(len(wordArr)):
    if wordArr[i] in lookup:
        # if i != len(wordArr)-1 and wordArr[i+1] not in lookup[wordArr[i]]: this is for no dupes
        if i != len(wordArr) -1:
            lookup[wordArr[i]].append(wordArr[i+1])
    else:
        if i != len(wordArr)-1:
            lookup[wordArr[i]] = [wordArr[i+1]]



# TODO: construct 5 random sentences
# Your code here

def random_sentence():
    s = ''
    start_word = wordArr[random.randint(0, len(wordArr)-1)]

    s+= start_word + ' '

    cur = lookup[start_word][random.randint(0, len(lookup[start_word])-1)]

    while True:
        s += cur + ' '

        cur = lookup[cur][random.randint(0, len(lookup[cur])-1)]
        # if re.match(r"^[A-Z][\w\s]+[?.!]$", cur):
        if cur.endswith('.') or cur.endswith('!') or cur.endswith('?') or cur.endswith('. ') or cur.endswith('! ') or cur.endswith('? '): # this still wont match every stop word for some reason
            s += cur + '\n'
            break
    return s


for i in range(6):
    print(random_sentence())


