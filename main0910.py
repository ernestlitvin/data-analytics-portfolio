##
import random
import string

# q_length = int(input("Enter the length of password:"))
# q_digits = int(input("How many digits should be in the password?"))
# q_symbols = int(input("How many symbols should be in the password?"))
# letters_length = 0
#
# if q_digits + q_symbols > q_length:
#     print("The sum of digits and symbols are bigger than the length of password")
# else:
#     letters_length = q_length - q_digits - q_symbols
#     print(f"Length of letters in password - {letters_length}")
#
#     r_digits = ""
#     for i in range(q_digits):
#         r_digits += random.choice(string.digits)
#
#     # r_digits = "".join(random.choice(string.digits) for x in range(q_digits)) ## best alternative way
#
#     print(f"Random digits in password - {r_digits}")
#
#     r_symbols = "".join(random.choice(string.punctuation) for x in range(q_symbols))
#     print(f"Random symbols in password - {r_symbols}")
#
#     r_letters = "".join(random.choice(string.ascii_letters) for x in range(letters_length))
#     print(f"Random letters in password - {r_letters}")
#
#     full_psw = r_digits + r_symbols + r_letters
#     print(f"Full password - {full_psw}")
#
#     final_psw = "".join(random.sample(full_psw, k=q_length))
#     print(f"Final shuffled password - {final_psw}")

print()
print("------")

# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”

for i in range(10):
    print("labas")

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

for i in range(0,10):
    print(i)

# Sukurkite masyvą iš dešimties augalų pavadinimų.

list = ["azuolas", "pusis", "berzas", "egle", "liepa", "klevas", "saulegraza", "ramune", "roze", "tulpe"]

# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

for i in range(10):
    print(list[i])

print()
print("-----")

# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
for i in reversed(range(10)):
    print(list[i])

print()
print("-----")

# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

for i in range(10,51,2):
    print(i)

print()
print("-----")

# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite.
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

for i in range(10,51,2):
    if i % 10 == 0:
        continue
    print(i)

print()
print("-----")
## Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
count_even = 0

for i in range(0,20):
    if i % 2 == 0:
        continue
        count_even += 1
    print(i)
    print(count_even)

