# nr_str1 = input("Please enter a random number: ")
# nr_fl1 = float(nr_str1)
# nr_str2 = input("Please enter a second random number: ")
# nr_fl2 = float(nr_str2)
# sym_str = input("Please enter a symbol (+,-,/,*): ")
#
# if sym_str == "+":
#     result = nr_fl1 + nr_fl2
#     print(f"The result is {result}")
# elif sym_str == "-":
#     result = nr_fl1 - nr_fl2
#     print(f"The result is {result}")
# elif sym_str == "/":
#     if nr_fl2 != 0:
#         result = nr_fl1 / nr_fl2
#         print(f"The result is {result}")
#     else:
#         print("The second number is 0")
# elif sym_str == "*":
#     result = nr_fl1 * nr_fl2
#     print(f"The result is {result}")
# else:
#     print("Invalid input")
import random

print()
# Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 25.
# Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

kin1 = random.randint(0,25)
kin2 = random.randint(0,25)
kin3 = random.randint(0,25)

print(kin1,kin2,kin3)
