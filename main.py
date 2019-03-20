import fileinput
from trie import Node

punctuation = ['.', '?', '!', ';', ',']
dict = Node('root')
searched = {}

# iterates through dictionary file and adds
# all words to a trie for fast searching
def loadDict():
    file = fileinput.input(files=('dictionary.txt')) 
    lineNo = 1
    wordsToSkip = ['ing', 'en', 'aut', 'de', 'ful', 'uti', 'n\'t', 'goe', 'dra', 'andra', '\'t','ble','eth', 'et']
    for l in file:
        line = l.strip()
        if "#!comment" not in line and line not in wordsToSkip and (len(line) > 2 or line == "a" or  line == "A" or line == "I" or lineNo <= 200):
            lineNo += 1
            dict.add(line)
    file.close()

# goes through and adds spaces around punctuation
# to increase accuracy of the program's output
def preProcess(str):
    res = []
    n = len(str)
    for i, c in enumerate(str):
        res.append(c)
        if c in punctuation and i != n -1:
            res.append(' ')
    return ''.join(res)

# iterates through array of possible words and
# converts to string with spaces
def extractWords(str, possibleWords, savedPunctuation):
    result = ""
    for i, val in enumerate(possibleWords):
        if possibleWords[i] != 0:
            start = i
            end = i + val
            result += str[start:end] + " "
    if savedPunctuation != "":
        result = result[:-1]
    return result + savedPunctuation

# searches trie for combinations of characters
# to form valid words
def insertSpace(str):
    n = len(str)
    savedPunctuation = ""
    if str[n-1] in punctuation:
        savedPunctuation = str[n-1] + " "
        str = str[:-1]
    
    n = len(str)
    possibleWords = [0] * n
    usedInidices = [n]
    i = n - 2
    
    while i >= 0:
        lastUnused = usedInidices[0]
        part = str[i:lastUnused]
        print(part, i, lastUnused)

        if dict.search(part, True):
            possibleWords[i] = lastUnused - i    
            usedInidices.insert(0,i)
            print(usedInidices)
            print(possibleWords)
            print('part', part, 'i',i, 'last unused', lastUnused)
        
        # if end is reached and first val is 0
        # we need to backtrack and undo the last
        # word we created
        if i == 0 and possibleWords[i] == 0:
            print('before reset', i, lastUnused)
            print(usedInidices)
            
            possibleWords[lastUnused] = 0
            lastUnused = usedInidices.pop(0)
            i = lastUnused - 1
            
            print(usedInidices)
            if len(usedInidices) == 0:
                usedInidices.append(n)
            
        else:
            i -= 1

    # when loop is done, get words from the 
    # array of indices of word beginnings
    return extractWords(str, possibleWords, savedPunctuation)
            
def main():
    # loads dictionary into trie
    loadDict()
    
    # reads from input file
    file = open("input.txt", "r")
    inputText = preProcess(file.readline()).split(' ')
    file.close()
    
    # iterates through sentences and 
    # writes them to output.text
    res = []
    for t in inputText:
        res.append(insertSpace(t))
    output = ''.join(res)
    
    print(output)
    file = open('output.txt', 'w+')
    file.write(output)
    file.close()

main()
