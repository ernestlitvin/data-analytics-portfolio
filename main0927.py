import pandas as pd
pokemon_df = pd.read_csv("pokemon.csv")
print(pokemon_df)
print("---")
# group_by_type = pokemon_df.groupby("Type 1")

mean_stats_by_type = pokemon_df.groupby("Type 1").mean(numeric_only = True)
print(mean_stats_by_type)

## more agr functions:
# .sum(): sum of meaning(s)
# .count(): count of record(s) (not empty)
# .min()/.max(): max/min meaning of record(s)
# .nunique(): count of unique record(s)
print("---")
pokemon_count_by_type = pokemon_df.groupby("Type 1")["ID"].count()
print(pokemon_count_by_type)