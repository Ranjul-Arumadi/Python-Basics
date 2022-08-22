a = [7,8,2,1,0,45]

a.sort()

size = len(a)
median =0
if size%2==0:
    median = ((size/2)+(size/2 +1))/2
else:
    median = size/2
    
print(median)