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

print("-------")

results = []
for numbers in range(1,3001):
    if numbers % 77 == 0:
        results.append(numbers)
print(", ".join(str(x) for x in results))






