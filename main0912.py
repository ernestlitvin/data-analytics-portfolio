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
# for index, value in enumerate(num):
#     print(f"Index: {index}, Number: {value}")

# Naudodamiesi 1 uždavinio masyvu:
# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
print("------")
print()
count10 = 0
for n in num:
    if n > 10:
        count10 += 1
print(f"Numbers count, which are bigger then 10 - {count10}")

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
# num = []
# for _ in range(30):
#     num.append(random.randint(5, 25))
print(num)
n_num = []

for index, values in enumerate(num):
    print(index, values)
    inval = values - index
    n_num.append(inval)
print(n_num)

# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
print("------")
print()

print(num)

for _ in range(10):
    num.append(random.randint(5, 25))
print(num)
print(len(num))

print("------")
print()
# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;




