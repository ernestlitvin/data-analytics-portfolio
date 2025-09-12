# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite
# kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
import random

print()
print("-----")

nr_count_150 = 0

for _ in range(300):
    num = random.randint(0, 300)
    if num > 150:
        nr_count_150 += 1
    if num > 275:
        print(f"[{num}]", end=" ")
        continue
    print(num, end=" ")
print()
print(f"Numbers, which are bigger than 150 - {nr_count_150}")

## alternative, better way

# skaiciai = []
# count = 0

# for _ in range(300):
#     skaicius = random.randint(1,300)
#     skaiciai.append(skaicius)
#     if skaicius > 150:
#         count += 1
#
# for skaicius in skaiciai:
#     if skaicius > 275:
#         print(f"[{skaicius}]", end=" ")
#     else:
#         print(skaicius, end=" ")
# print()
# print("Number of values greater than 150:", count)

print()
print("------")

# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

nums = []
#
for nr in range(1,3001):
    if nr % 77 == 0:
        nums.append(nr)

print(nums)
print(", ".join(str(x) for x in nums)) ## best solution

print()
print("-------")

# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.

# for _ in range(5):
#     print("* "*5)

for row in range(5):
    for col in range(5):
        print("* ", end=" ")
    print()

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.
print("-------")

# (0,0) (0,1) (0,2) (0,3) (0,4)
# (1,0) (1,1) (1,2) (1,3) (1,4)
# (2,0) (2,1) (2,2) (2,3) (2,4)
# (3,0) (3,1) (3,2) (3,3) (3,4)
# (4,0) (4,1) (4,2) (4,3) (4,4)

for x in range(5):
    for y in range(5):
        if x == y or x + y == 4:
            print("# ", end=" ")
        else:
            print("* ", end=" ")
    print()

print("-------")
print()
# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;
count_herb = 0
count_nr = 0

# for _ in range(5):
#     num = random.randint(0, 1)
#     print(num, end=" ")
#     if num == 0:
#         count_herb += 1
#     elif num == 1:
#         count_nr += 1
#
# print()
# print(f"Herb count - {count_herb}")
# print(f"Number count - {count_nr}")

# Iškritus herbui;

while True:
    num = random.randint(0, 1)
    if num == 0:
        print("H")
        break
    elif num == 1:
        print("N")
print("-----")

# Tris kartus iškritus herbui;
count_herb = 0
count_nr = 0
while True:
    num = random.randint(0, 1)
    if num == 1:
        print("N", end = " ")
    elif num == 0:
        count_herb += 1
        print("H", end = " ")
        if count_herb == 3:
            break

# Tris kartus iš eilės iškritus herbui;
count_nr = 0
const_herb = 0

while True:
    num = random.randint(0, 1)
    if num == 1:
        const_herb = 0
        print("N", end = " ")
    elif num == 0:
        const_herb += 1
        print("H", end = " ")
        if const_herb == 3:
            break

## need to finish more

