# Your code here

from os import path
import re

def histo(file):

    words = ''
    with open(path.abspath('applications/histo/{}'.format(file))) as f:
        words = f.read()
    words = re.sub(r"[^\w\s']+", '', words)

    words = re.sub(r"(\r\n|\r|\n|\t)", ' ', words)

    words = words.split(' ')

    lookup = {}

    for word in words:
        if word == ' ' or word == '':
            continue
        word = word.lower()
    
        if word in lookup:
            lookup[word] +=1
        else:
            lookup[word] = 1

    sortedArr = sorted(lookup.items(),key=lambda x: (-x[1], x[0]))

    leftAlign = ''

    # find longest word
    for item in sortedArr:
        if len(item[0]) > len(leftAlign):
            leftAlign = item[0]


    for item in sortedArr:
        char = '#'*item[1]
        print(item[0].ljust(len(leftAlign)+2), char)


histo('robin.txt')


    

