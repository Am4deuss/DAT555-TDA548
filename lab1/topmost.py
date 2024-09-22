import io
import sys
import importlib.util
import urllib.request
import wordfreq

def readFile(): # function that reads file if the 2nd argument is a textfile
    file = open(sys.argv[2], encoding="utf-8")
    readData = file.read()
    lines = readData.split("\n")
    file.close()
    return lines

def main(): # main program function

    with open(sys.argv[1], encoding="utf-8") as inp_file: # built-in fuction which opens the stopfile (file is specified as the 1st argument when launching program)
        stopWords = wordfreq.tokenize(inp_file) # produces list of words to ignore in count

    if sys.argv[2].startswith("https://") or sys.argv[2].startswith("http://"): # checks if the 2nd argument is a textfile or website. if website -> read website
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
    else:
        lines = readFile()

    n = int(sys.argv[3])

    # explained in wordfreq.py
    words = wordfreq.tokenize(lines)
    wordCount = wordfreq.countWords(words, stopWords)
    wordfreq.printTopMost(wordCount, n)

main()