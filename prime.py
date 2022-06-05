a = int(input("Enter value: "))

for i in range(2, (a//2)+1):            #check till n/2 + 1
    if a % i == 0:
        print("Not Prime")
        print('{0} times {1} is {2}'.format(i, (a//i), a))
        exit()

print("Prime")