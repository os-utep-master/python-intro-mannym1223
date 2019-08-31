import re
import os
import sys
import string
# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

#make sure text file exists
if not os.path.exists(inputFname):
    print ("text file input %s doesn't exist! Exiting" % inputFname)
    exit()

with open("declaration.txt", "r") as countFile:
    #reads entire file as a string
    #converts all characters to lowercase
    #removes all punctuation from the string
    #splits string into separate words
    data = re.sub(r'[^\w]', " ", countFile.read().lower()).split()

wordCounts = {}

for word in data:
    if word not in wordCounts.keys():
        #create a key for the word if does not exist
        wordCounts.update({word : 0})
    wordCounts[word] += 1

#sort all the words alphabetically
sortedWords = sorted(wordCounts.keys())

with open("output.txt", "w") as outputFile:
    for word in sortedWords:
        outputFile.write(word + " " + str(wordCounts[word]) + "\n")
