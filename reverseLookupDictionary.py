a = {'a' : 1, 'b':2, 'c':3}

keysValue = 1

out = []

for key, value in a.items():
    if value == keysValue:
        out.append(key)
    #print(key, value)

print(out)