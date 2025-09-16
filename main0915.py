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
set_diff = my_set1 - my_set2
list3 = list(set_diff)

print(list3)
print(len(list3))

# Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.
print("-----")
print()

match = my_set1 & my_set2
list4 = list(match)
print(list4)

# Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25.
# Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.
print("-----")
print()

list5 = []

for _ in range(2):
    num = random.randint(5,25)
    list5.append(num)
print(list5)

for _ in range(8):
    new_val = list5[-1] + list5[-2]
    list5.append(new_val)
print(list5)



