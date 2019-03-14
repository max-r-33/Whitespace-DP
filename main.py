from collections import OrderedDict
from trie import Node

import fileinput

dict = OrderedDict()
results = []

def loadDict():
    file = fileinput.input(files=('dictionary.txt')) 
    for l in file:
        line = l.strip()
        if "#!comment" not in line and (len(line) > 1 or line == "a" or  line == "A" or line == "I"):
            dict[line.strip()] = fileinput.lineno()
    file.close()

def addSpace(str, result):
    length = len(str)
    for i in range(1, length+1):
        part = str[0:i]
        if part in dict:
            if i == length:
                result += part
                results.append(result)
                return
            addSpace(str[i:length+1], result + part + " ")

def main():
    loadDict()
    file = open("input.txt", "r")
    text = file.readline()
    file.close()
    addSpace(text, "")
    results.reverse()
    for result in results:
        print(result)

main()
