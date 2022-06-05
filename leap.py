'''

400 and 100
4 and not 100

else not leap year
'''

a= int(input("Enter year: "))

if (a%400==0) and (a%100==0):
    print("Leap year")
elif (a%4==0) and (a%100!=0):
    print("Leap year")
else:
    print("Not leap year")