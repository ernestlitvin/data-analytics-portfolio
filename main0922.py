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

print("----")
print()

solar = pd.Series(
    data = [4879, 12104, 12742, 6779, 139822],
    index = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
)
print(solar)
print("----")
print()

games = {
"Name" : ["The Witcher 3: Wild Hunt", "Counter-Strike: Global Offensiv", "Minecraft", "Cyberpunk 2077"],
"Year" : [2015, 2012, 2011, 2020],
"Genre" : ["RPG", "FPS", "Survival", "Action RPG"]
}
games_df = pd.DataFrame(games)
print(games_df)
print("----")
print(f"Size of table {games_df.shape}")
print("----")
print(f"Collums names: {games_df.columns}")
print("----")
print("Type of data in collums: ")
print(games_df.dtypes)

print("----")
print()
pokemon_df = pd.read_csv("pokemon.csv")
print(pokemon_df)
print("----")
print(pokemon_df.head(3)) ## first three lines
print("----")
print(pokemon_df.tail(3))  ## last three lines
print("----")
pokemon_df.info() ## all information about table
print("----")
print(pokemon_df.describe())

## 1 task
df = pd.read_csv("pokemon.csv")
print(df)
print(df.head(5))
print("----")
## 2 task
df.info() ## "type 2" missing 2 meanings
## task 3
print("----")
print(df.describe()) ## max defense is 90
index = False
df.to_csv("pokemon_for_colleague.csv", index = False)


