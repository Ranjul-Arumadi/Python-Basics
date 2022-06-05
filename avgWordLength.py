a = input("Enter string: ")
b = a.split()
maxSizeIndex = 0
size = 0
count = 0
temp =0

for word in b:
    if len(word) > temp:
        temp = len(word)
        maxSizeIndex = count
    size  = size+ len(word)
    count +=1

avg = size/count
bigWord = b[maxSizeIndex]

print("Avg: {0} \nBig Word = {1}".format(avg, bigWord))
