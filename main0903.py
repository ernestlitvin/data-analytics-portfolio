import random

print("Start of practice 09-03")

name = "Erikas"
age = 32
city = "Vilnius"

print("hello world!")
print("my name is")
print(name)

age_in_5_years = age + 5
print("In 5 years, I will be")
print(age_in_5_years)

is_over_21 = age > 21
print("Am I over 21 ?")
print(is_over_21)

movie_title = "Titanic"
release_year = 1997
raiting = 8.6
current_year = 2025

print("Film " + movie_title + "(" + str(release_year) + ")" + " has rating " + str(raiting))
print("Film was released " + str((current_year) - (release_year)) + " years ago")

first_name = "Erikas"
last_name = "Latvenas"
full_name = first_name + " " + last_name
city = "Vilnius"

print(f"My name is {first_name} {last_name}")
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(f"I live in {city} and it has {len(city)} letters")

# user_name = input("What is your name? ")
# rndnr_str = input("Please tell the number from 1 to 10")
# rndnr_int = int(rndnr_str)
# rndnr_str2 = input("Please tell another number from 11 to 20")
# rndnr_int2 = int(rndnr_str2)
# print(f"Hello, {user_name}!")
# print(rndnr_int + rndnr_int2)
# sum_rndnr = rndnr_int + rndnr_int2
#
# print(f"Sum of your numbers is {sum_rndnr}")

# Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus).
# Parašykite kodą, kuris pagal gimimo metus paskaičiuotų jūsų amžių ir
# naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".

name = "Erikas"
surname = "Latvenas"
birth_year = 1993
current_year = 2025
age = current_year - birth_year
print(f'My name is {name} {surname}. I am {age} years old.')

my_list = [1, "hello", True]
print(my_list)
first_thing = my_list[2]
print(first_thing)
my_list.append("bye")
print(my_list)
print(len(my_list))
#----#
print()

nrs = [10,21,36,44,57,64,75]
print(nrs[2])
nrs.append(80)
print(nrs)

age = 19
if age >= 20:
    print("Access granted")
else:
    print("Access denied")

print()

# print()
# age_str = input("What is your age?")
# age_int = int(age_str)
# if age_int >= 18:
#     print("Welcome")
# elif age_int >14 and age_int <=17: #elif 14 <= age_int <= 17: - alternative way
#     print("Access only with parents")
# else:
#     print("Access denied")

# Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.
import random

rnd_nr1 = random.randint(0,4)
rnd_nr2 = random.randint(0,4)
print(rnd_nr1)
print(rnd_nr2)

if rnd_nr1 > rnd_nr2:
    if rnd_nr2 != 0:
        result = rnd_nr1/rnd_nr2
        print(round(result, 2))
    else:
        print("The min number is 0")
elif rnd_nr1 < rnd_nr2:
    if rnd_nr1 != 0:
        result = rnd_nr2/rnd_nr1
        print(round(result,2))
    else:
        print("The min number is 0")
else:
    print("Numbers are equal")

#asd