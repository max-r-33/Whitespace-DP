class Node():

    def __init(self, val):
         self.val = val         # the contents of the node
         self.children = []     # array of children nodes
         self.endOfWord = False # whether this node is the end, tells us to stop searching
         self.counter = 1       # keeps track of how many words contain this character

    def add(self, root, word):
        node = root
        for character in word:
            foundInChild = False
            for child in node.children:
                if child.val == character:
                    child.counter += 1
                    node = child
                    foundInChild = True
                    break
            if not foundInChild:
                new_node = Node(val)       # create new node 
                node.children.append(new_node)  # add this new node to be a child of the current node
                node = new_node                 # set the current node to be the new node
        node.endOfWord = True
    
    def search(self, root, text):
        node = root
        if root.children:
            for character in text:
                charFound = False
                for child in node.children:
                    if child.val == character:
                        charFound = True
                        node = child
                if not charFound:
                    return 0
        else:
            return 0
        return True