import pandas as pd

lst = ['a', 'b', 'c']

df1 = pd.DataFrame(lst)
print(df1)

dct = {'name': ['a', 'b'], 'age' :[11,22]}

df2 = pd.DataFrame(dct)
print(df2)