# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from os import path
lookup = {}

enLookup = [
    'E',
    'T',
    'A',
    'O',
    'H',
    'N',
    'R',
    'I',
    'S',
    'D',
    'L',
    'W',
    'U',
    'G',
    'F',
    'B',
    'M',
    'Y',
    'C',
    'P',
    'K',
    'V',
    'Q',
    'J',
    'X',
    'Z']


def findFrequency(file):
    text = ''
    with open(path.abspath('applications/crack_caesar/{}'.format(file))) as f:
        text = f.read()
    
    for char in text:
        if char == ' ':
            continue
        if char in enLookup:
            if char in lookup:
                lookup[char] += 1
            else:
                lookup[char] = 1

    sortedArr = sorted(lookup.items(), key=lambda x: x[1], reverse=True)
    
    anotherLook ={}
    i = 0

    for item in sortedArr:
        anotherLook[item[0]] = enLookup[i]
        i+=1

    newText = ''

    for char in text:
        if char in lookup:
            newText += anotherLook[char]
        else:
            newText += char

    print(newText)



findFrequency('ciphertext.txt')




