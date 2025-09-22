import pandas as pd

student_grades_names = pd.Series(
    data = [5, 4, 3, 5, 4],
    index = ["Jonas", "Monika", "Gintare", "Agne", "Kotryna"]
)
print(student_grades_names)
