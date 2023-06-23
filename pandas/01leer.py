import pandas as pd

df = pd.read_excel('sample.xlsx')

print(df)
print(df['El Salto (Tumbes)'].describe())
