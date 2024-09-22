import io
import sys
import importlib.util
import urllib.request
import wordfreq

def readFile():
    file = open(sys.argv[2], encoding="utf-8")
    readData = file.read()
    lines = readData.split("\n")
    file.close()
    return lines

def main():

    with open(sys.argv[1], encoding="utf-8") as inp_file:
        stopWords = wordfreq.tokenize(inp_file)

    if sys.argv[2].startswith("https://") or sys.argv[2].startswith("http://"):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
    else:
        lines = readFile()

    n = int(sys.argv[3])

    words = wordfreq.tokenize(lines)
    wordCount = wordfreq.countWords(words, stopWords)
    wordfreq.printTopMost(wordCount, n)

main()