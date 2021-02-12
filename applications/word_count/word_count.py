import re

def word_count(s):
    # Your code here
    s = re.sub(r"[^\w\s']+", '', s)

    s = re.sub(r"(\r\n|\r|\n|\t)", ' ', s)


    if len(s) < 1:
        return {}

    lookup = {}

    stringArr = s.split(' ')


    for words in stringArr:
        word = words.lower()

        if word == ' ' or word == '':
            continue

        if word in lookup:
            lookup[word] +=1
        else:
            lookup[word] = 1


    return lookup





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello!"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))