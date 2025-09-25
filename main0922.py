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
df.to_csv("pokemon_for_colleague.csv", index=False)
print("----")
print()

names = pokemon_df["Name"] # choose specific col
print(names)
print("----")
stats = pokemon_df[["Name", "Attack", "Defense"]] ## few col-s
print(stats)
print("----")
names_via_dot = df.Name # if no spaces in the name of col - legit to use
print(names_via_dot)
## .loc[] (location)
## .iloc[] (integer location)
## in () -> always go rows, then coll (1,2)
print("----")
first_pokemon = pokemon_df.iloc[0]
print(first_pokemon)
print("----")
middle_pokemons = pokemon_df.iloc[1:3]
print(middle_pokemons)
print("----")
cell_value = pokemon_df.iloc[0,1]
print(cell_value)
print("-----")
mewtwo = pokemon_df.loc[3]
print(mewtwo)
print("----")
subset = pokemon_df.loc[2:4, ["Name", "HP"]]
print(subset)
print("----")
high_attack_condition = pokemon_df["Attack"] > 80
print(high_attack_condition)
print("----")
strong_pokemons = pokemon_df[high_attack_condition] ## or strong_pokemons = pokemon_df[pokemon_df['Attack'] > 80]
print(strong_pokemons)
print("----")
is_legendary = pokemon_df["Legendary"] == True
high_def = pokemon_df["Defense"] > 70
print("----")
unique_pokemon = pokemon_df[is_legendary & high_def]
print(unique_pokemon)
## or
## legendary_and_tough = df[(df['Legendary'] == True) & (df['Defense'] > 70)]
## print(legendary_and_tough)
print("----")
pokemon_cards = pokemon_df[["Name", "Type 1", "HP"]]
print(pokemon_cards)
print("----")
third = pokemon_df.iloc[2]
print(third)
print("----")
fast_pokemons = pokemon_df["HP"] > 90
hp_pokemons = pokemon_df[fast_pokemons]
print(hp_pokemons)
print("----")
print("grass-and-posion")
# pokemon_df["Type 1"] == "Grass"
# pokemon_df["Type 2"] == "Poison"
grass_and_poison = pokemon_df[(pokemon_df["Type 1"] == "Grass") & (pokemon_df["Type 2"] == "Poison")]
print(grass_and_poison)
print("----")
pokemon_df["Total"] = pokemon_df["HP"] + pokemon_df["Defense"] + pokemon_df["Attack"]
print(pokemon_df)
print(pokemon_df.head())
print("----")
df_without_total = pokemon_df.drop(columns=["Total"]) ## df.drop('Total', axis=1)
print(df_without_total)
print("----")
pokemon_df["Type 2"] = pokemon_df["Type 2"].fillna("Single Type")
print(pokemon_df)
print("----new---")
duplicate_example = pd.DataFrame({
    "letter": ["a", "b", "a"],
    "number": [1, 2, 1]
})
print("---before duplicates---")
print(duplicate_example)
print("----")
no_duplicates = duplicate_example.drop_duplicates()
print("---after duplicates---")
print(no_duplicates)

