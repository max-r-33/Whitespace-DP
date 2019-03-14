import fileinput
from trie import Node

dict = Node('root')
searched = {}

def loadDict():
    file = fileinput.input(files=('dictionary.txt')) 
    for l in file:
        line = l.strip()
        if "#!comment" not in line and (len(line) > 1 or line == "a" or  line == "A" or line == "I"):
            dict.add(line)
    file.close()

def addSpace(str):
    if dict.search(str):
        return str
    l = len(str)
    for i in range(l, 1, -1):
        start = str[:i]
        if dict.search(start):
            ending = str[i:]
            endWSpaces = addSpace(ending)
            if endWSpaces != None:
                print(start + " " + endWSpaces)
                return start + " " + endWSpaces

def main():
    # loads dictionary into trie
    loadDict()
    
    # reads from input file
    file = open("input.txt", "r")
    inputText = file.readline()
    file.close()

    print("Input: ", inputText)
    addSpace(inputText)

main()
