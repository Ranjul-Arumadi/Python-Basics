def prime(num, i):
    if(num==i):
        return True
    elif num%i==0:
        return False
    else:
        return prime(num, i+1)

print(prime(44,2))