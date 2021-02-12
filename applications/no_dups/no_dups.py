def no_dups(s):
    # Your code here
    lookup = {}

    if len(s) <=1:
        return s

    stringArr = s.split(' ')

    newString = ''
    for i in range(len(stringArr)):
        if stringArr[i] not in lookup:
            if i == 0:
                newString += stringArr[i] 
            else:
                newString += ' ' + stringArr[i]
            lookup[stringArr[i]] = 1
    return newString




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))