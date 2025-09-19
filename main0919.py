import pandas as pd

s = pd.Series([10, 20, 30])
print(s)
# Output:
# 0    10
# 1    20
# 2    30
# dtype: int64

sales = pd.Series([250, 300, 450], index=['Январь', 'Февраль', 'Март'])
print(sales)
# Output:
# Январь     250
# Февраль    300
# Март       450
# dtype: int64

# Создание DataFrame из словаря
data = {
    'Имя': ['Анна', 'Борис', 'Виктор'],
    'Возраст': [28, 34, 29],
    'Город': ['Москва', 'СПб', 'Новосибирск']
}
df = pd.DataFrame(data)
print(df)
print("------")
# df - наш DataFrame из примера выше
print(df.shape)
print("-----") # Output: (3, 3)
df.info()
print("------")
# Выбрать всех, кто старше 30 лет
older_than_30 = df[df['Возраст'] > 30]
print(older_than_30)
# Выбрать всех из Москвы
moscow_people = df[df['Город'] == 'Москва']
print(moscow_people)

print("---NEW----")

# Создадим DataFrame с продажами
sales_data = {
    'Менеджер': ['Иван', 'Анна', 'Иван', 'Петр', 'Анна'],
    'Регион': ['Запад', 'Восток', 'Запад', 'Запад', 'Восток'],
    'Продажи': [100, 150, 200, 50, 250]
}
sales_df = pd.DataFrame(sales_data)
print(sales_df)
print("------")

# Сгруппируем по менеджеру и посчитаем сумму продаж для каждого
manager_sales = sales_df.groupby('Менеджер')['Продажи'].sum()
print(manager_sales)
print("------")
# Можно группировать по нескольким столбцам и применять несколько функций
region_manager_sales = sales_df.groupby(['Регион', 'Менеджер']).agg({'Продажи': ['sum', 'mean']})
print(region_manager_sales)

print("------")
print()

books = {
    "Title" : ["To Kill a Mockingbird", "The Great Gatsby", "Moby Dick"],
    "Author" : ["Harper Lee", "F. Scott Fitzgerald", "Herman Melville"],
    "Year" : ["1960", "1925", "1851"],
    "Pages" : ["281", "180", "635"]
}

books_df = pd.DataFrame(books)
print(books_df)
print("------")
two_coll = books_df.iloc[0]
print(two_coll)