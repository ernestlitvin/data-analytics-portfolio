def function_with_print(a, b):
    print(a + b) # Просто показывает результат

def function_with_return(a, b):
    return a + b # Возвращает результат для дальнейшего использования

result1 = function_with_print(5, 10) # На экране напечатается 15
# Но в переменной result1 теперь лежит None (ничего)

result2 = function_with_return(5, 10) # На экране ничего не напечатается
# Но в переменной result2 теперь лежит число 15
print(result2 * 2) # Мы можем использовать результат. Выведет 30.

def print_list_items(items):
    for item in items:
        print(item)

my_plants = ["Роза", "Тюльпан"]
print_list_items(my_plants) # Передаем список в функцию

# Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.
print()
print("-----")

def sum_and_print(a, b):
    result = a + b
    print(result)
sum_and_print(5, 10)

# alternative way
# def suma(a, b):
#     return a + b
# print(suma(10,20))

## additionally like an example
# result = suma(10, 20)
# final_result = result * 2
# print(final_result) # Выведет 60

# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
print()
print("-----")

def PISq():
    return 9.8596
print(PISq())

