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

# daily_revenue_before = full_df.groupby("transaction_date")["Revenue"].sum()
# print(daily_revenue_before)
daily_revenue = full_df.groupby("transaction_date")["Revenue"].sum().reset_index() ## reset_index() is very important.
# It is a bridge that translates data from the "result of grouping" format to the "table ready for visualization" format.
# print("---")
# print(daily_revenue)

# sns.lineplot(data=daily_revenue, x="transaction_date", y="Revenue")
# plt.title("Revenue by Transaction Date")
# plt.xticks(rotation=15) # Rotate dates for better readability
# plt.show()
# ## Purpose: Ideal for tracking changes of a numerical variable in time.
# # Helps answer the question: "How did the indicator change day by day?".
#
# sns.lineplot(data=full_df, x="transaction_date", y="Revenue", hue = "category", estimator = "sum")
# plt.title("Revenue by Transaction Date and Category")
# plt.xticks(rotation=15)
# plt.show()
## if we want to look at the dynamics of each category of products separately - hue parameter can solve it.
# estimator='sum' is an important parameter that tells lineplot to add values, not count the average.

# numeric_cols = full_df[["quantity", "price_per_item", "Revenue"]]
# correlation_matrix = numeric_cols.corr()
# print("--Correlation Matrix--")
# print(correlation_matrix)
#
# sns.heatmap(correlation_matrix, annot=True) # annot=True - very useful parameter, it signs values in cells
# plt.title("Heatmap of Correlation Matrix")
# # plt.show()
# ## Purpose: Visualizes a matrix where the color of the cell depends on its value.
# # Ideal for displaying correlations or summary tables.




print("--tasks--")
# sns.scatterplot(data=full_df, x="price_per_item", y="quantity")
# plt.show() # clients are buying cheapest products more often, than expensive
# sns.histplot(data=full_df, x="quantity")
# plt.show() # 1-2
# sns.countplot(data=full_df, x="product_name")
# plt.show() # notebook is more popular
#
# sns.barplot(data=full_df, x="category", y="quantity")
# plt.show() # books cat. is more popular
# sns.boxplot(data=full_df, x="price_per_item", y="category")
# plt.title("What is the price per item in certain category ?")
# plt.show() # The graph shows that the price per unit of a product in the category "Electronics" is much higher than in others.
# # Even if people buy 1-2 units of electronics, the total revenue will be huge due to the high price.
# sns.barplot(data=full_df, x="customer_id", y="Revenue", orient="v")
# plt.show() # 502 and 504 are more valuable customers
#
daily_quantity = full_df.groupby("transaction_date")["quantity"].sum().reset_index()
sns.lineplot(data=daily_quantity, x="transaction_date", y="quantity")
plt.title("Total Quantity by Transaction Date")
plt.xticks(rotation=15)
# plt.show()

sns.lineplot(data=full_df, x="transaction_date", y="Revenue", hue = "customer_id")
plt.title("Total Revenue by Customer ID")
plt.xticks(rotation=15)
# plt.show()

pivot = pd.pivot_table(full_df,
                       values='Revenue',
                       index='category',
                       columns='transaction_date',
                       aggfunc='sum',
                       fill_value=0)
sns.heatmap(pivot,annot=True)
plt.show()







