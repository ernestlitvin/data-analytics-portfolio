# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999.
# Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).
import random
list1 = []
list2 = []

while len(list1) < 100:
    num1 = random.randint(100, 999)
    if num1 not in list1:
        list1.append(num1)
print(list1)

while len(list2) < 100:
    num2 = random.randint(100, 999)
    if num2 not in list2:
        list2.append(num2)
print(list2)

# alternative way
# numbers1 = random.sample(range(100, 999), 100)
# number2 = random.sample(range(100, 999), 100)
#
# print(numbers1)
# print(number2)

# Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve,
# bet nėra antrame 6 uždavinio masyve.
print("-----")
print()

my_set1 = set(list1)
my_set2 = set(list2)
list3 = my_set1 - my_set2
print(list3)
print(len(list3))


