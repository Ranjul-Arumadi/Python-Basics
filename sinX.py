import math

x = int(input("Enter the value of x : "))
c = int(input("Enter the count : "))
sum=0
j=1
for i in range(1,c+1):
 if(i==1 or i%2!=0 ):
  sum+=(pow(x,j)/math.factorial(j))
 else:
  sum-=(pow(x,j)/math.factorial(j))
 j+=2
print(sum)
