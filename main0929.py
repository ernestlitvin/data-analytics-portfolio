import pandas as pd #1.1
#1.2
transactions_df = pd.read_csv("transactions.csv")
products_df = pd.read_csv("products.csv")

print("\n--- Table with products components ---")
print(products_df)
print("\n--- Table with transactions info ---")
print(transactions_df)
print('------')
print(transactions_df.head(5)) #1.3
print("----")
transactions_df.info() #1.4
print("---Describe of transactions table---")
print(transactions_df.describe()) #1.5
price_per_item_mean = transactions_df["price_per_item"].mean().round(0)
transactions_df["price_per_item"] = transactions_df["price_per_item"].fillna(price_per_item_mean) # 2.1
print(transactions_df["price_per_item"])

