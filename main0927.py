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
print("---")
# .agg() -> few operations
summary_by_type = pokemon_df.groupby("Type 1").agg(
    avg_attack = ("Attack", "mean"),
    max_defense = ("Defense", "max"),
    pokemon_count = ("Name", "count")
)
print(summary_by_type)
print("---")
sales_df = pd.read_csv("sales.csv")
print(sales_df)
print("--sum of sales--")
manager_sales = sales_df.groupby("Manager")["Sales"].sum()
print(manager_sales)
print()
print("--max sales by region--")
max_sales_by_region = sales_df.groupby("Region")["Sales"].max()
print(max_sales_by_region)
print()
print("--count by product --")
count_by_product = sales_df.groupby("Product").count()
print(count_by_product)


