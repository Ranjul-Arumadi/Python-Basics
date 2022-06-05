f = open("z.txt", 'a')
f.write("Hello there!")

f.close()

f = open("z.txt", 'r')
text = f.read()
print(text)