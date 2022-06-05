f = open("z.txt", 'r')

lines = 0
word = 0
chars = 0

for line in f:
    a = line.split()
    word = word + len(a)

    for item in a:
        chars = chars + len(item)
    lines = lines + 1
    
f.close()

print("lines: "+ str(lines))
print("words: "+ str(word))
print("characters: "+ str(chars))