import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sns.set()
full_df = pd.read_csv("full_df.csv")

# sns.scatterplot(data = full_df, x="quantity", y="Revenue", hue="category") # Purpose: Shows the relationship between two numerical variables.
# Helps answer the question: "When one variable grows, what happens to the other?".
# plt.show()

# sns.histplot(data = full_df, x="Revenue") # histplot. Purpose: Shows the distribution of a single numerical variable.
# # Helps answer the question "Which values are most common?".
# plt.show()

# sns.countplot(data=full_df, x="category") # Purpose: Displays the number of entries for each category in a categorical column.
# # This is value_counts() graphically.
# plt.show()

# sns.barplot(data=full_df, x="category", y="Revenue")
# plt.title("Avg revenue per category") # Add a header using Matplotlib
# plt.show()
# Shows the average (default) value of the numeric variable for each category.
# Ideal for answering the question: "In which group is the average higher?".

# sns.boxplot(data=full_df, x="category", y="Revenue")
# plt.title("Distribution of revenues by categories")
# plt.show()
## boxplot - "Box with a mustache" 📦
# Purpose: This is a more powerful tool than barplot. It shows the full distribution of the numerical variable within each category.
# Helps answer the questions: "What is the median? How big is the spread? Are there emissions?".
# How to read "box":
# The line inside the box is the median (50% less values, 50% more).
# Box boundaries are the 25th and 75th percentiles (data center).
# "Moustache" - shows the main spread of data.
# Points outside the mustache are emissions (abnormally high or low values).

print("--tasks--")
# sns.scatterplot(data=full_df, x="price_per_item", y="quantity")
# plt.show() # clients are buying cheapest products more often, than expensive
# sns.histplot(data=full_df, x="quantity")
# plt.show() # 1-2
# sns.countplot(data=full_df, x="product_name")
# plt.show() # notebook is more popular

