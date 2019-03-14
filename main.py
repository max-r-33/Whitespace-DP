import fileinput
from trie import Node

root = Node('root')

def loadDict():
    file = fileinput.input(files=('dictionary.txt')) 
    for l in file:
        line = l.strip()
        if "#!comment" not in line and (len(line) > 1 or line == "a" or  line == "A" or line == "I"):
            root.add(line)
    file.close()

# def addSpace(str, result):
#     length = len(str)
#     for i in range(1, length+1):
#         part = str[0:i]
#         if root.search(part):
#             if i == length:
#                 print(part)
#             # addSpace(str[i:length+1], result + part + " ")

def main():
    loadDict()
    # root.pprint()
    file = open("input.txt", "r")
    inputText = file.readline()
    file.close()

main()
