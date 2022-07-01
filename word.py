def getWordSet():
    filename = 'words.txt'
    words = []
    file = open(filename, 'r')
    for line in file.readlines():
        words.append(line.strip().upper())
    file.close()
    return words