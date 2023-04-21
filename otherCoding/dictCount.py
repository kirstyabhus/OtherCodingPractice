file = open("sentence.txt", "r")
text = file.read().split()
count = dict()

for word in text:
    count[word] = count.get(word, 0) + 1
print(count)

# gives key vale pirs
for aa,bb in count.items():
    print(aa,bb)