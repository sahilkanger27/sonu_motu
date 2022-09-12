import pandas as pd

df = pd.read_excel("03_Data.xlsx")
print(df)
# Cleaning the data - Dropping rows will null values
df1 = df.dropna()
print(df1)

df1.plot(x='robots_owned', y='total_playtime', style='o')
