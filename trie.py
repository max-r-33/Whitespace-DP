import sys

class Node:

    def __init__(self, val):
        self.val = val         # the contents of the node
        self.children = {}     # dictionary of children nodes for ~ O(1) lookup
        self.endOfWord = False # whether this node is the end, tells us to stop searching
        
    def add(self, word):
        node = self
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                new_node = Node(character)          # create new node 
                node.children[character] = new_node # add this new node to be a child of the current node
                node = new_node                     # set the current node to be the new node
        node.endOfWord = True

    # If requireFullWord is true, then the function will only return true 
    # when the last character searched is the end of the word. 
    # Otherwise, prefixes will return true, this is the default behavior
    def search(self, text, requireFullWord = False):
        node = self
        if node.children:
            for character in text:
                if character in node.children:
                    node = node.children[character]
                else:
                    return False
        else:
            return False
        if requireFullWord == True and node.endOfWord == False:
            return False
        return True


    def pprint(self, indent="", last=True, stack=""):
        if indent != "":
            stack = stack + self.val

        sys.stdout.write(indent)
        if last:
            sys.stdout.write("|-")
            indent += "  "
        else:
            sys.stdout.write("|-")
            indent += "| "

        sys.stdout.write("{}".format(self.val))
        if self.endOfWord:
            print(" - {}".format(stack))
        else:
            print()

        for i, c in enumerate(self.children):
            self.children[c].pprint(indent, i == len(self.children) - 1, stack)
