def tokenize(lines): # function which takes a parameter containing a list of sentences as elements

    words = [] # empty list for storing words

    for line in lines: # loops through content (in this case sentences) of list "lines"

        start = 0

        while start < len(line): # while loop, ends when all characters of sentence are checked
            if not line[start].isspace(): # checks if current character is NOT a space
                if line[start].isalpha(): # if current character is a LETTER -> while loop to check if next character is also a letter until FALSE. when FALSE -> append word to list "words"
                    end = start
                    while line[end].isalpha():
                        end += 1
                        if end >= len(line): # correcting index error, if last charcther of sentence is a LETTER we have to check so that we dont select a character that does not exist. For example "this is a test sentence", if we are currently on the word "sentence" at the last letter "e" we have to make sure to not check the next character of the sentence since it does not exist. Otherwise we could end up with the following error: "index out of range"
                            break
                    words.append(line[start:end].lower())
                    start = end
                elif line[start].isdigit(): # if current character is a DIGIT -> while loop to check if next character is also a digit until FALSE. when FALSE -> append sequence of digits to list "words"
                    end = start
                    while line[end].isdigit():
                        end += 1
                        if end >= len(line): # correcting index error, just like letter but instead digits
                            break
                    words.append(line[start:end])
                    start = end
                else: # if current character is neither a LETTER or a DIGIT -> current character is a "symbol" -> append current symbol to list "words"
                    words.append(line[start])
                    start += 1
            else: # if space -> ignore, goto next character
                start += 1 

    return words # return list of words

def countWords(words, stopWords): # function which takes parameters "words" (list of words from function "tokenize()") and "stopwords" (list of words to not include in count)
    countDict = {} # creating empty dictionary
    for i in words: # loops through every word in list "words"
        if not i in stopWords: # if current word in list "stopWords" -> exclude
            if not i in countDict: # if current word is has not yet been counted -> add word to dictionary with value 1
                countDict[i] = 1
            else: # if current word is already in dictionary -> increment current value by 1
                countDict[i] = countDict[i] + 1
    
    return countDict # return dictionary with key "word" and value "frequency"

def printTopMost(frequencies,n): # function which takes parameters "frequencies" (dictionary of words with key "word" and value "frequency") and "n" (how many frequencies which should be printed in the end)

    if len(frequencies) < n: # checks if there are enough entries in dictionary "frequencies" to print "n"-amount. if NOT -> print as many entries as possible
        n = len(frequencies)

    wordTuples = [] # empty list to store key + value from "frequencies" as tuples. (key, value) instead of {"key"->value}

    for word,freq in frequencies.items(): # loops through "frequencies"-dictionary and creates tuples of keys and values -> appends to list "wordTuples"
        wordTuples.append((word,freq))

    wordTuples = sorted(wordTuples, key = lambda x: -x[1]) # sorts list "wordTuples" by value of the tuples (which are located at index[1] in each tuple)

    for i in range(0,n): # loops n-amount of times and prints the most frequent words
        w = wordTuples[i][0]
        w = w.ljust(20)
        f = str(wordTuples[i][1])
        f = f.rjust(5)
        print(w + f)


