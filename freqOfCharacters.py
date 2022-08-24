input = "raanjul"

dict={}

for letter in input:
    if letter in dict:
        dict[letter] +=1
    else:
        dict[letter] = 1
        
print(str(dict))
