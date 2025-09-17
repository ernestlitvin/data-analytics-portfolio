# Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
# mass = [1, "hello", 2.5, True, 10, -20, -55.5]
# def numbers_checker(mass):
#     for item in mass:
#         if isinstance(item, (int, float)) and not isinstance(item, bool):
#             print(item)
# numbers_checker(mass)

# Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius.
# (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius
# ar skaičius su kableliu.
print()
print("-----")

def whole_number(massive, print_only_integers=True):
    print(f"--- Print only whole = {print_only_integers} ---")
    for item in massive:
        if print_only_integers == True:
            if isinstance(item, int) and not isinstance(item, bool) :
                print(item, end=" ")
        else:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                print(item, end=" ")
    print("\n")

massive = [-534.3, -200, -12.4, 0, 1, 5, 21, 543, 23.5, 453.3, "dog", "no", True, False ]
whole_number(massive, True)
whole_number(massive, False)

## Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.
def word_count(text):
    text = text.split()
    return len(text)
print(word_count("How many words in this sentence?"))