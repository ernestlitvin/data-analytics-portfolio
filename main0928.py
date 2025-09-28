import pandas as pd

## pd.concat() — simple "glue" pages (vertically)

# Employee table
staff_df = pd.DataFrame({
    'employee_id': [101, 102, 103, 104],
    'name': ['John', 'Mary', 'Tom', 'Ann'],
    'department': ['IT', 'HR', 'IT', 'Marketing']
})
# Salary table (no Mary (102), but there is a new employee - 105)
salary_df = pd.DataFrame({
    'employee_id': [101, 103, 104, 105],
    'salary': [70000, 80000, 60000, 90000]
})
print("--- Employees ---")
print(staff_df)
print("\n--- Salary ---")
print(salary_df)

# example: the new record of the new employee
new_staff_df = pd.DataFrame({
    'employee_id': [106],
    'name': ['Sergio'],
    'department': ['IT']
})
# "Glue" old and new table (vertical)
all_staff = pd.concat([staff_df, new_staff_df])
print(all_staff)

## pd.merge() — SQL's JOIN analog
## Syntax : pd.merge(left_table, right_table, on='key_table', how='тип_объединения')
# how (join's type') — most important parametr:
# inner (internal) (default): Leaves only those rows for which there is a key in both tables.
# left (left): Take all the rows from the left table. If any of them do not match to the right, there will be blanks - NaN.
# right (right): Reverse, all rows are taken from the right table.
# outer (full): Takes all rows from both tables.
print("\n--- Merged Employees & Salary ---")
merged_inner = pd.merge(staff_df, salary_df, on="employee_id")
print(merged_inner)
merged_left = pd.merge(staff_df, salary_df, on="employee_id", how="left")
print("\n")
print(merged_left)
# merged_left["salary"] = merged_left["salary"].fillna("Unknown")
# print(merged_left)
merged_outer = pd.merge(staff_df, salary_df, on="employee_id", how="outer")
print("\n")
print(merged_outer)



