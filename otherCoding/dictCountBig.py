file = open("sentence.txt", "r")
text = file.read().split()
counts = dict()

for word in text:
    counts[word] = counts.get(word, 0) + 1

bigWord = None
bigCount = None

for aKey, aValue in counts.items():
    if bigCount is None or bigCount < aValue:
        bigWord = aKey
        bigCount = aValue

print(bigWord, bigCount)
