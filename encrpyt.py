pwd = input()

dist = int(input())
out=""
ascii = 0

for letter in pwd:
    ascii = ord(letter)
    ascii = ascii+dist
    out = out + chr(ascii)
    
print(out)
