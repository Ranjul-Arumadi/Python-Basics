a = int(input("Enter number to be checked: "))
temp = a
digit = 0
armstrong = 0

while temp > 0:
    digit = temp % 10
    armstrong += digit**3
    temp = temp//10

if armstrong == a:
    print("Armstrong")
else:
    print("Not armstrong")
