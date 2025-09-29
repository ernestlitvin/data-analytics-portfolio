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
electronics_sale = full_df[full_df["category"] == "Electrics"] # 4.1
print(electronics_sale)
big_rev = full_df[full_df["Revenue"] > 10000] # 4.2
print(big_rev)
sum_rev_by_cat = full_df.groupby("category")["Revenue"].sum() # 5.1
print("---Sum of Revenues by category---")
print(sum_rev_by_cat)
prod_qua_per_client = full_df.groupby("customer_id")["quantity"].mean() # 5.2
print("\n--- Mean product quantity per client  ---")
print(prod_qua_per_client)