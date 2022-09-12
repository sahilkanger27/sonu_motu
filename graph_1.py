import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("03_Data.xlsx")
print(df)

# Cleaning the data - Dropping rows will null values
df1 = df.dropna()
print(df1)

plt.scatter(df1['ch_fights'], df1['total_playtime'])
plt.show()
