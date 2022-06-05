import math

x = int(input("Enter the value of x : "))
c = int(input("Enter the count : "))
sum=0
for i in range(0,c+1):
 sum+=(pow(x,i)/math.factorial(i))
print(sum)
