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

# Naudodamiesi 1 uždavinio masyvu:
# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
print("------")
print()

