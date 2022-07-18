row = int(input("Enter row: "))
col = int(input("Enter col: "))

arr = []

print("Enter values: ")
for i in range(row):
    column = []
    for j in range(col):
        a = int(input())
        column.append(a)
    arr.append(column)

print(arr)

