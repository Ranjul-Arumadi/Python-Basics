a = input("Enter string: ")
b = int(input("Enter index: "))

ans = a.replace(a[b], '', 1)   # if 1 is not given all occurences will be replaced!
print(ans)

#OR

'''
ans = a[0:b] + a[b+1:]
print(ans)
'''