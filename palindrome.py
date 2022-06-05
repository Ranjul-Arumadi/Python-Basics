a = int(input("Enter value: "))
temp = a
digit = 0
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev*10+digit
    temp = temp//10

if rev == a:
    print("Palindrome")
else:
    print("Not palindrome")