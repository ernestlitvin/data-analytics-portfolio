import pandas as pd

print("------")
print()

books = {
    "Title" : ["To Kill a Mockingbird", "The Great Gatsby", "Moby Dick"],
    "Author" : ["Harper Lee", "F. Scott Fitzgerald", "Herman Melville"],
    "Year" : [1960, 1925, 1851],
    "Pages" : [281, 180, 635]
}

books_df = pd.DataFrame(books)
print(books_df)
print("------")
# two_coll = books_df.head(2)
# print(two_coll)
# two_coll = books_df.loc[0:1] ## alternative way
# print(two_coll)
print("-----")
# books_df.info()

print()
print("----")
title = books_df["Title"]
print(title)
print("-----")
two_rows = books_df[["Title", "Author"]]
print(two_rows)
print("-----")
third_b = books_df.loc[2]
print(third_b)
print("-----")
after_1900 = books_df[books_df["Year"] > 1900]
print(after_1900)
print("----")
books_df["Age"] = 2025 - books_df["Year"]
books_df["Genere"] = "Classic"
print(books_df)
print("----")
sorted_books_df = books_df.sort_values(by='Year')
print(sorted_books_df)

