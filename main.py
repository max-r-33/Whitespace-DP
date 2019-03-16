import fileinput
from trie import Node

dict = Node('root')
searched = {}

def loadDict():
    file = fileinput.input(files=('dictionary.txt')) 
    lineNo = 1
    for l in file:
        line = l.strip()
        if "#!comment" not in line and (len(line) > 2 or line == "a" or  line == "A" or line == "I" or lineNo <= 200):
            lineNo += 1
            dict.add(line)
    file.close()

def insertSpace(str):
    n = len(str)
    possibleWords = [0] * n
    usedInidices = [n]
    i = n-2
    
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
        
        # if end is reached an first val is 0
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
    print(possibleWords)

            
def main():
    # loads dictionary into trie
    loadDict()
    
    # reads from input file
    file = open("input.txt", "r")
    inputText = file.readline()
    file.close()

    print("Input: ", inputText)
    insertSpace(inputText)

main()
