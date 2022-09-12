import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("03_Data.xlsx")
print(df)

# Cleaning the data - Dropping rows will null values
df1 = df.dropna()
print(df1)

# Championship fight mode vs Robots owned
plt.scatter(df1['ch_fights'], df1['robots_owned'])
plt.show()

# Free sparring fight mode vs Robots owned
plt.scatter(df1['fs_fights'], df1['robots_owned'])
plt.show()

# Time arcade fight mode vs Robots owned
plt.scatter(df1['ta_fights'], df1['robots_owned'])
plt.show()
