f = open('z.txt', 'r')
sum = 0
for line in f:
    numList = line.split()
    for num in numList:
       number = int(num)
       sum = sum+number

print('Sum = {0}'.format(sum))
f.close()