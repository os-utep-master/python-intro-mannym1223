import re

with open("declaration.txt", "r") as countFile:
    #reads entire file as a string
    #converts all characters to lowercase
    #removes all punctuation from the string
    #splits string into separate words
    data = re.sub(r'[^\w\s]', "", countFile.read().lower()).split()

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
