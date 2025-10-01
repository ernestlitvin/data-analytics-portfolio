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
##### The basic syntax that you need to keep in mind is matrix[strike_rows, strike_columns].
# Each of these slices follows the rule -> start:stop:step
matrix = np.arange(25).reshape(5, 5)
print("Invg mаtrix:\n", matrix)

# 1. Basic cuts (rectangular cuts)
center_square = matrix[1:4,1:4]
print(f"\nCenter square matrix:\n", center_square)

# 2. Open sections (from beginning till end)
# You can miss "start" or "stop" to make a cut from the very beginning or to the very end of the axis.
# : - means "take everything on this axis".
# :n - means "take everything from the beginning till element n (not including)".
# n: - means "take everything from element n (including) to the end".

top_left_corner = matrix[:3,:2]
print(f"\nTop left:\n", top_left_corner)
buttom_right_corner = matrix[2:,3:]
print(f"\nButton right corner:\n", buttom_right_corner)

# 3. Slices with step (step)
# This is the most powerful tool. It allows you to "jump" through elements. Syntax: start:stop:step.

every_2nd_column = matrix[:,::2]
print(f"\nEvery 2nd column:\n", every_2nd_column)
checkboard = matrix[::2, ::2] # every 2nd row and every 2nd column
print(f"\nCheckboard:\n", checkboard)

# 4. Changing values through slices
# One of the coolest features of NumPy - you can not only "read" data through a slice, but also "write" into it.
matrix_copy = matrix.copy()
matrix_copy[3:, 3:] = 99
print(f"\nMatrix copy with edited corner:\n", matrix_copy)
######### basic functions ###############
arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])
sum_arr = arr1 + arr2
print(f"\nSum of arrays:\n", sum_arr)
diff_arr = arr1 - arr2
print(f"\nDifference of arrays:\n", diff_arr)
prod_arr = arr1 * arr2
print(f"\nProduct of arrays:\n", prod_arr)
div_arr = arr1 / arr2
print(f"\nDivision of arrays:\n", div_arr)
print(arr2 * 2)
print(arr2 ** 2)
### universal functions "ufuncs" ###
arr = np.array([1,4,9,16])
# Calculate the square root of each element
print(f"\nSquare root of arr:\n {np.sqrt(arr)}")
# Calculate the exponent for each element (e^x)
print(f"\nExponent of arr:\n {np.exp(arr)}")
# Calculate sin for each element
print(f"\nSin:\n {np.sin(arr)}")
# The list of such functions is huge: np.log(), np.abs(), np.cos() and many others.
# You don’t need to write cycles, NumPy does all the dirty work for you, and it does it lightning fast.
### tasks ###
# 1
prices_usd = np.array([10, 25, 50, 75, 100])
eur_rate = np.array (0.85)
prices_eur = prices_usd * eur_rate
print(f"\nEuro prices:\n {prices_eur}")
# 2
heights_m = np.array([1.75, 1.80, 1.65, 1.90])
weights_kg = np.array([70, 85, 60, 95])
