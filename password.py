isDigit = 0
isUpper = 0
isSpecial = 0

pwd = input("Enter password: ")
if len(pwd)>8:
    for i in pwd:
        if str(i).isdigit():
            isDigit+=1
        elif str(i).isupper():
            isUpper+=1
        elif not str(i).isalnum():
            isSpecial +=1
else:
    print("fail")
    exit()

if (isUpper>=1 and isSpecial>=1 and isDigit>=1):
    print("Pass")
    exit()
else:
    print("Fail")
    exit()
