from trie import Node

def main():
    root = Node('root')
    Node.add(root, "bear")
    Node.add(root, "bell")
    Node.add(root, "bid")
    Node.add(root, "bull")
    Node.add(root, "buy")
    Node.add(root, "sell")
    Node.add(root, "stock")
    Node.add(root, "stop")

    # print(root.search("hac"))
    # print(root.search("hack"))

    
    root.pprint()
main()
