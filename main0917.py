# Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.

mass = [1, "hello", 2.5, True, 10]

def numbers_checker(mass):
    for item in mass:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            print(item)
numbers_checker(mass)

