lines = ["The 10 little chicks"]

def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            if not line[start].isspace():
                if line[start].isalpha():
                    end = start
                    while line[end].isalpha():
                        end += 1
                        if end >= len(line):     #Fin fullösning
                            break
                    words.append(line[start:end].lower())
                    start = end
                elif line[start].isdigit():
                    end = start
                    while line[end].isdigit():
                        end += 1
                        if end >= len(line):     #Fin fullösning
                            break
                    words.append(line[start:end])
                    start = end
                else:
                    words.append(line[start])
                    start += 1
            else:
                start += 1 

    
    return words

def countWords(words, stopWords):
    countDict = {}
    for i in words:
        if not i in stopWords:
            if not i in countDict:
                countDict[i] = 1
            else:
                countDict[i] = countDict[i] + 1
    
    return countDict

def printTopMost(frequencies,n):
    if len(frequencies) < n:
        n = len(frequencies)
    wordTuples = []
    for word,freq in frequencies.items():
        wordTuples.append((word,freq))
    wordTuples = sorted(wordTuples, key = lambda x: -x[1])
    for i in range(0,n):
        w = wordTuples[i][0]
        w = w.ljust(20)
        f = str(wordTuples[i][1])
        f = f.rjust(5)
        print(w + f)


