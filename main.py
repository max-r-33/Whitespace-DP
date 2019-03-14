def loadDict():
    dict = {}

    file = open("dictionary.txt", "r")
    lines = file.readlines()
    rank = 1
    
    for l in lines:
        line = l.strip()
        if "#!comment" not in line and (len(line) > 1 or line == "a" or  line == "A" or line == "I"):
            dict[line.strip()] = rank
            rank += 1

    file.close()
    return dict

def checkSentence(text, dict):
    for start in range(0, len(text)):
        for end in range(start + 1, len(text)):
            part = text[start:end]
            if part in dict:
                print('true', part)

def main():
    dict = loadDict()
    file = open("input.txt", "r")
    text = file.readline()
    file.close()
    checkSentence(text, dict)

main()
