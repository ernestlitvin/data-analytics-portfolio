# Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.

mass = [1, "hello", 2.5, True, 10]

def numbers_checker(mass):
    for num in mass:
        if num == isinstance(num, int):
            print(num)

numbers_checker(mass)

