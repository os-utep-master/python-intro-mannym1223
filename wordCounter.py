import re
with open("declaration.txt", "r") as countFile:
    data = re.sub(r"^\w", "", countFile.read().lower()).split()

wordCounts = {}

for word in data:
    if word not in wordCounts.keys():
        wordCounts.update({word : 1})
    wordCounts[word] += 1

with open("output.txt", "w") as outputFile:
    for word in wordCounts.keys():
        print(word + " " + str(wordCounts[word]))
