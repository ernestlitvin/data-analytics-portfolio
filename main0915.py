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

