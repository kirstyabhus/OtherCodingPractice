file = open("xy.txt", "r")
count = 0

for line in file:
    line = line.strip()
    if not(line.startswith("From")):
        continue
    count += 1
    words = line.split()
    email = words[1]
    print(email)
print(count)