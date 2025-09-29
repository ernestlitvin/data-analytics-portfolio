import pandas as pd #1.1
#1.2
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
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
transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"]) # 2.2
transactions_df = transactions_df.drop_duplicates() # 2.3
transactions_df["Revenue"] = transactions_df["quantity"] * transactions_df["price_per_item"] # 2.4
full_df = pd.merge(transactions_df, products_df, on = "product_id", how = "left") # 3.1,2
print("\n--- Table with all components ---")
print(full_df)
# electronics_sale = full_df[(full_df["transaction_date"]) & (full_df["category" == "Electronics"])]
td = full_df["transaction_date"]
cat = full_df["category"] == "Electrics"
elec = full_df[(full_df["transaction_date"]) & (full_df["category"] == "Electrics")]
print(elec)
