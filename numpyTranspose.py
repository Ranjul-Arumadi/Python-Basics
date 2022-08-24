import numpy as np

r1 = int(input())
c1 = int(input())

    
arr1 = []
for i in range(r1):
    col1 = []
    for j in range(c1):
        col1.append(int(input()))
    arr1.append(col1)
    
a = np.array(arr1)
c = np.transpose(a)

print(c)
