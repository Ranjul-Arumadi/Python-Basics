import pandas as pd

ds = pd.read_csv('test.csv', encoding = 'unicode_escape')

print(ds.to_string())