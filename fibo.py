a = int(input("Enter limit: "))

first = 0
second = 1
third = 0

print("0 1", end =' ')
for i in range(a-2):
    third = first + second
    print(third, end=' ')
    first = second
    second = third