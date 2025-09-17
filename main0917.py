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

# Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
# Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.
print()
print("-----")
def filtered_numbers(massi, print_only_even = True):
    filtered_list = []
    for item in massi:
        if print_only_even == True:
            if item % 2 == 0:
                filtered_list.append(item)
        else:
            if item % 2 != 0:
                filtered_list.append(item)
    return filtered_list

massi = [1,2,3,4,5,6,7,8,9,10,11,12]
fil_even = filtered_numbers(massi, True)
fil_odd = filtered_numbers(massi, False)
print(f"Even numbers - {fil_even}")
print(f"Odd numbers - {fil_odd}")

# Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.
print()
print("-----")
def number_is_prime(num):
    if num < 2:
        return False
    for item in range(2, num - 1):
        if num % item == 0:
            return False
    else:
        return True
print(f"Is 5 is prime? {number_is_prime(5)}")
print(f"Is 9 is prime? {number_is_prime(9)}")
print(f"Is 2 is prime? {number_is_prime(2)}")

# Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.
print()
print("-----")

def number_in_square(a,b):
    return (a ** b)
sq = number_in_square(5,3)
print(sq)

# Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik nepasikartojančius elementus
print()
print("-----")
def unique_list(numbers_list):
    new_list = []
    for item in numbers_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

numbers_list = [1,1,2,3,4,5,6,7,8,8,9,10,11,12,12]
ex = unique_list(numbers_list)
print(ex)
## alternative way
# def unique_list(list_of_numbers):
#     return list(set(list_of_numbers))
# list_of_numbers = [1,2,2,3,4,5,5,6,7,8,9,10,10,11,12]
# ex = unique_list(list_of_numbers)
# print(ex)

# Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.
print()
print("-----")

def most_repeated_letter(text):
    letter_counts = {}
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    print(max(letter_counts, key=letter_counts.get))
most_repeated_letter("nu nu ir nereikia")

# Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.
print()
print("-----")

def longest_word(text):
    text = text.split()
    longest_word = ""
    length_word = 0
    for word in text:
        if len(word) > length_word:
            length_word = len(word)
            longest_word = word
    print(longest_word)
longest_word("kaip visiems o man nieko neduoda gospadoris kukuliukas-makaliukas")

## alternative way
# def longest_word_short(text):
#     words = text.split()
#     longest = max(words, key=len)
#     print(longest)
# longest_word_short("kaip visiems o man nieko neduoda gospadoris kukuliukas-makaliukas")

