import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sns.set()
full_df = pd.read_csv("full_df.csv")

sns.scatterplot(data = full_df, x="quantity", y="Revenue", hue="category")
plt.show()


