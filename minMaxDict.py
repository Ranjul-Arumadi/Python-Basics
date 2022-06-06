a = {'a':1,'b':2,'c':3}

maxVal = max(a.keys(), key = lambda k:a[k])
print(maxVal)