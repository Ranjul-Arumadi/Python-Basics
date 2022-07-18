import numpy as np

row = int(input("Enter row: "))
col = int(input("Enter row: "))

arr = []
for i in range(row):
    colmn = []
    for j in range(col):
        colmn.append(int(input()))
    arr.append(colmn)

a = np.array(arr)

row1 = int(input("Enter row: "))
col1 = int(input("Enter row: "))

arr1 = []
for i in range(row):
    colmn1 = []
    for j in range(col):
        colmn1.append(int(input()))
    arr1.append(colmn1)


b = np.array(arr1)
if(col == row1):
    c = np.multiply(a,b)
    print(c)
else:
    print("error")

