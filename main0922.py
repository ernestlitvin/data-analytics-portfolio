import pandas as pd

student_grades_names = pd.Series(
    data = [5, 4, 3, 5, 4],
    index = ["Ignas", "Monika", "Gintare", "Agne", "Kotryna"]
)
print(student_grades_names)
print("----")
data = {
"Name" : ["Ignas", "Monika", "Gintare", "Agne", "Kotryna"],
"Age" : [21, 43, 18, 33, 26],
"City" : ["Vilnius", "Kaunas", "Klaipeda", "Vilnius", "Utena"]
}
employees_df = pd.DataFrame(data)
print(employees_df)
print("----")
print(f"Table size: {employees_df.shape}")
print(f"Collums names: {employees_df.columns}")
print("Type of data in collums:")
print(employees_df.dtypes)



