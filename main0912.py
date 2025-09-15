# Генерируем уникальные числа, пока их не наберется 10
import random

unique_numbers = []
while len(unique_numbers) < 10:
    new_num = random.randint(1, 20)
    if new_num not in unique_numbers:
        unique_numbers.append(new_num)

print(unique_numbers)
print("------")
print()
# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
num = []
for _ in range(30):
    num.append(random.randint(5, 25))
print(num)
print(len(num))
print(num[0])

# num = [random.randint(5, 25) for _ in range(30)] ## alternative way

# Naudodamiesi 1 uždavinio masyvu:
# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
print("------")
print()
count10 = 0
for n in num:
    if n > 10:
        count10 += 1
print(f"Numbers count, which are bigger then 10 - {count10}")

## count10 = sum(1 for n in num if n > 10) ## alternative way

# Raskite didžiausią masyvo reikšmę;
print("------")
print()
maxi = max(num)
print(maxi)

# Suskaičiuokite visų reikšmių sumą;
print("------")
print()
suma = sum(num)
print(suma)

# Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;
print("------")
print()

print(num)
n_num = []

for index, values in enumerate(num):
    print(index, values)
    inval = values - index
    n_num.append(inval)
print(n_num)

## n_num = [value - index for index, value in enumerate(num)] ## alternative way

# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
print("------")
print()

print(num)

for _ in range(10):
    num.append(random.randint(5, 25))
print(num)
print(len(num))

## new_elements = [random.randint(5, 25) for _ in range(10)] ## alternative way
## num += new_elements # or num.extend(new_elements)

print("------")
print()
# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;
print(num)
odd_in = []
even_in = []

for index, values in enumerate(num):
    if index % 2 == 0:
        even_in.append(values)
    else:
        odd_in.append(values)
print(even_in)
print(odd_in)

## even_in = num[::2]   # alternative way
## odd_in = num[1::2]

# Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
print()
print("------")
print()

null_num = []

for index, values in enumerate(num):
    if index % 2 == 0 and values > 15:
        values = 0
        null_num.append(values)
    else:
        null_num.append(values)
print(num)
print(null_num)

# alternative way
# for index in range(len(num)):
#     if index % 2 == 0 and num[index] > 15:
#         num[index] = 0

# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
print()
print("------")
print()

for index, values in enumerate(num):
    if values > 10:
        break
print(num)
print(index)

# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.
print()
print("------")
print()

let_list = []
abcd = ["A","B","C","D"]

for _ in range(20):
    rnd = random.choice(abcd)
    let_list.append(rnd)
print(let_list)

print(f" Letter A count - {let_list.count("A")}")
print(f" Letter B count - {let_list.count("B")}")
print(f" Letter C count - {let_list.count("C")}")
print(f" Letter D count - {let_list.count("D")}")

# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.

fixed = sorted(let_list)
print(fixed)

# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes.
# (turi gautis masyvas, kurio elementai, kaip pvz atrodo taip: “AAB”, “CBC”, “DDA”, 200 reikšmių).
# Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.
print()
print("------")
print()

list1 = []
list2 = []
list3 = []
final_list = []

for _ in range(100):
    let = random.choice(abcd)
    list1.append(let)
print(list1)

for _ in range(100):
    let = random.choice(abcd)
    list2.append(let)
print(list2)

for _ in range(100):
    let = random.choice(abcd)
    list3.append(let)
print(list3)

for i in range(100):
    indeks = list1[i] + list2[i] + list3[i]
    final_list.append(indeks)
print(f"All combinations - {final_list}")

my_set = set(final_list)
print(f"The final unique list of combinations - {my_set}")
print(f"The amount of combinations - {len(my_set)}")
