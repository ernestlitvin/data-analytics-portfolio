# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# sns.set()
# full_df = pd.read_csv("full_df.csv")
#
# sns.scatterplot(data = full_df, x="quantity", y="Revenue", hue="category") # Purpose: Shows the relationship between two numerical variables.
# # Helps answer the question: "When one variable grows, what happens to the other?".
# plt.show()
#
# sns.histplot(data = full_df, x="Revenue") # histplot. Purpose: Shows the distribution of a single numerical variable.
# # Helps answer the question "Which values are most common?".
# plt.show()
#
# sns.countplot(data=full_df, x="category") # Purpose: Displays the number of entries for each category in a categorical column.
# # This is value_counts() graphically.
# plt.show()
#
# sns.barplot(data=full_df, x="category", y="Revenue")
# plt.title("Avg revenue per category") # Add a header using Matplotlib
# plt.show()
# # Shows the average (default) value of the numeric variable for each category.
# # Ideal for answering the question: "In which group is the average higher?".
#
# sns.boxplot(data=full_df, x="category", y="Revenue")
# plt.title("Distribution of revenues by categories")
# plt.show()
# ## boxplot - "Box with a mustache" 📦
# # Purpose: This is a more powerful tool than barplot. It shows the full distribution of the numerical variable within each category.
# # Helps answer the questions: "What is the median? How big is the spread? Are there emissions?".
# # How to read "box":
# # The line inside the box is the median (50% less values, 50% more).
# # Box boundaries are the 25th and 75th percentiles (data center).
# # "Moustache" - shows the main spread of data.
# # Points outside the mustache are emissions (abnormally high or low values).
#
# daily_revenue_before = full_df.groupby("transaction_date")["Revenue"].sum()
# print(daily_revenue_before)
# daily_revenue = full_df.groupby("transaction_date")["Revenue"].sum().reset_index() ## reset_index() is very important.
# It is a bridge that translates data from the "result of grouping" format to the "table ready for visualization" format.
# print("---")
# print(daily_revenue)
#
# sns.lineplot(data=daily_revenue, x="transaction_date", y="Revenue")
# plt.title("Revenue by Transaction Date")
# plt.xticks(rotation=15) # Rotate dates for better readability
# plt.show()
# ## Purpose: Ideal for tracking changes of a numerical variable in time.
# # Helps answer the question: "How did the indicator change day by day?".
# #
# sns.lineplot(data=full_df, x="transaction_date", y="Revenue", hue = "category", estimator = "sum")
# plt.title("Revenue by Transaction Date and Category")
# plt.xticks(rotation=15)
# plt.show()
# # if we want to look at the dynamics of each category of products separately - hue parameter can solve it.
# estimator='sum' is an important parameter that tells lineplot to add values, not count the average.
#
# numeric_cols = full_df[["quantity", "price_per_item", "Revenue"]]
# correlation_matrix = numeric_cols.corr()
# print("--Correlation Matrix--")
# print(correlation_matrix)
# #
# sns.heatmap(correlation_matrix, annot=True) # annot=True - very useful parameter, it signs values in cells
# plt.title("Heatmap of Correlation Matrix")
# plt.show()
# # ## Purpose: Visualizes a matrix where the color of the cell depends on its value.
# # # Ideal for displaying correlations or summary tables.
#
# print("--tasks--")
# sns.scatterplot(data=full_df, x="price_per_item", y="quantity")
# plt.show() # clients are buying cheapest products more often, than expensive
# sns.histplot(data=full_df, x="quantity")
# plt.show() # 1-2
# sns.countplot(data=full_df, x="product_name")
# plt.show() # notebook is more popular
# #
# sns.barplot(data=full_df, x="category", y="quantity")
# plt.show() # books cat. is more popular
# sns.boxplot(data=full_df, x="price_per_item", y="category")
# plt.title("What is the price per item in certain category ?")
# plt.show() # The graph shows that the price per unit of a product in the category "Electronics" is much higher than in others.
# # Even if people buy 1-2 units of electronics, the total revenue will be huge due to the high price.
# sns.barplot(data=full_df, x="customer_id", y="Revenue", orient="v")
# plt.show() # 502 and 504 are more valuable customers
# #
# daily_quantity = full_df.groupby("transaction_date")["quantity"].sum().reset_index()
# sns.lineplot(data=daily_quantity, x="transaction_date", y="quantity")
# plt.title("Total Quantity by Transaction Date")
# plt.xticks(rotation=15)
# plt.show()
#
# sns.lineplot(data=full_df, x="transaction_date", y="Revenue", hue = "customer_id", estimator = "sum")
# plt.title("Total Revenue by Customer ID")
# plt.xticks(rotation=15)
# plt.show()
#
# pivot = pd.pivot_table(full_df,
#                        values='Revenue',
#                        index='category',
#                        columns='transaction_date',
#                        aggfunc='sum',
#                        fill_value=0)
# sns.heatmap(pivot,annot=True)
# plt.show()

################################---NumPy---################################

import numpy as np

python_list = [1,2,3,4,5]
numpy_array = np.array(python_list)
print(f"Simple python list: {python_list}")
print(f"Numpy list: {numpy_array}")
python_matrix = [[1,2,3],[4,5,6]]
numpy_matrix = np.array(python_matrix)
print(f"Numpy matrix:\n", numpy_matrix)
print("\n")
## np.arange(start, stop, step): Python’s analog range() but creates the NumPy array.
arr1 = np.arange(10)
print(arr1)
## np.zeros(shape): Creates an array of the specified form, filled with zeros.
arr2 = np.zeros((2,3))
print("\n",arr2)
## np.ones(shape): Same, but with ones.

matrix = np.array([[1, 2, 3], [4, 5, 6]])
# Array's shape (number of rows, number of columns)
print(f"Form (shape): {matrix.shape}") # (2, 3)
# Data element type
print(f"Data type (dtype): {matrix.dtype}") # int64
# Number of measurements (axes)
print(f"Number of measurements (ndim): {matrix.ndim}") #2

print("\n") # 1
pyth_list = [10,11,12,13,14,15]
vector = np.array(pyth_list)
print(vector)
print("\n", vector.shape)
matriks = np.zeros((3,3)) # 2
print("\n",matriks)
print("\n", matriks.ndim)
# 3
progression = np.arange(2,11,2)
print("\n",progression)
print(progression.dtype)
print("\n")

vector1 = np.arange(10,20)
print(f"Basic: \n",vector1)
first_element = vector1[0]
print(first_element)
last_element = vector1[-1]
print(last_element)
slice_1 = vector1[1:4]
print(slice_1)
slice_2 = vector1[2:] # from 2nd till end
print(slice_2)
slice_3 = vector1[:5] # first 5 items
print(slice_3)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Basic:\n", matrix)
element = matrix[1, 2]
print(f"\nItem in row 1, and column 2: {element}")
top_left = matrix[0, 0]
print(f"Item in row 0, and column 0: {top_left}")
print("Basic:\n", matrix)
sub_matrix1 = matrix[0:2]
print(f"\nFirst two rows:\n", sub_matrix1)
sub_matrix2 = matrix[:, 1:3]
print(f"\nRows 2 and 3:\n", sub_matrix2)
row = matrix[1,:] # or just matrix[1]
print(f"\nSecond row:\n", row)
column = matrix[:,0]
print(f"\nFirst column:\n", column)

## Tasks 2 ##
practice_matrix = np.arange(1, 13).reshape(3, 4)
print(f"\nPractice matrix:\n", practice_matrix)
# reshape(x,y) is a convenient method that "transforms" a one-dimensional array [1, 2, ..., 12] into a 3x4 matrix.
# 1
last_item = practice_matrix[2,3]
print(f"\nLast item: {last_item}")
# 2
second_row = practice_matrix[1,:]
print(f"\nSecond row:\n", second_row)
# 3
third_col = practice_matrix[:,2]
print(f"\nThird column:\n", third_col)
# 4
mat_in_mat = practice_matrix[1:3,2:4]
print(f"\nPractice matrix:\n", mat_in_mat)


