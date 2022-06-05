a = int(input("Enter number: "))
if a>=0:
    fact=1
else:
    print("No fact")
    exit()
while a>0:
    fact = fact*a
    a-=1

print(fact)