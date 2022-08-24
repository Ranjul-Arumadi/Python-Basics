# importing pandas as pd 
import pandas as pd 
# dictionary of lists 
# creating a dataframe from a dictionary 
df = pd.DataFrame([[1,' Linus Torvalds','Finland','Linux Kernel ',1991],
 [2,'Tim Berners-Lee','England','World Wide Web',1990],
 [3,'Guido van Rossum','Netherlands','Python',1991]],
columns=['SN','Name','Country','Contribution','Year'])

print()
print("Data frame with defaut index:")
print()
print(df)


df=df.set_index('SN')

print()
print("Data frame with SN as index:")
print()
print(df)

df.to_csv('inventors.csv')
