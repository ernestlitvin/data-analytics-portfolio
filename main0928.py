import pandas as pd

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
