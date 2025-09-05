# ##Order and discounts app
#
# subtotal = float(input("What is total sum of your order ?"))
# member = input("Are you a member ? yes/no").lower()
#
# is_member = False
# if member == "yes":
#     is_member = True
#
# if subtotal < 100:
#     shipping_cost = 10
# else:
#     shipping_cost = 0
#
# if subtotal >= 50:
#     discount = 5
# else:
#     discount = 0
#
# if is_member:
#     member_discount = 10
# else:
#     member_discount = 0
#
# print("Order price: ", subtotal)
# print("Discount: ", float(discount + member_discount))
# print("Shipping cost: ", float(shipping_cost))
# print("-----------------")
# print("Total price is: ", float(subtotal + shipping_cost - member_discount - discount))
import random

#####
numbers = [-12, -5, 1, 505, 1403, 22042, 1235334]
for number in numbers:
    if number > 0 and number % 2 == 0:
        print(f"The needed number was found {number}.")
#####
numbers = [2, 5, 14, 54]
total_sum = 0
for number in numbers:
    total_sum += number
print(total_sum)
#####
print()
#####
numbers = [-12, -5, 1, 23, 56, 89, 121]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)
print()
######
print("_____")
source_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
doubled_numbers = []

for number in source_number:
    number *= 2
    doubled_numbers.append(number)
print(doubled_numbers)
print()
######
print("_____")

# vowel = ['a', 'e', 'i', 'o', 'u']
# vowel_count = 0
#
# text = input("Please tell something").lower()
#
# for letters in text:
#     if letters == "a":
#         vowel_count += 1
#     elif letters == "e":
#         vowel_count += 1
#     elif letters == "i":
#         vowel_count += 1
#     elif letters == "o":
#         vowel_count += 1
#     elif letters == "u":
#         vowel_count += 1
# print(vowel_count)

print("_____")
### alternative way
# vowel_count = 0
# text = input("Please tell something").lower()
# vowel = "aeiou"
#
#
# for letters in text:
#     if letters in vowel:
#         vowel_count += 1
#
# print(f"Found {vowel_count} vowels in -{text}-")
print()
######
print("_____")

# Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 25.
# Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

a = random.randint(0,25)
b = random.randint(0,25)
c = random.randint(0,25)
print(a, b, c)

if b <= a <= c or c <= a <= b:
    print(a)
elif a <= b <= c or c <= b <=a:
    print(b)
else:
    print(c)

# if a <= b <= c:
#     print(b)
# elif b <= c <= a:
#     print(c)
# elif c <= a <= b:
#     print(a)
# elif a <= c <= b:
#     print(c)
# elif b <= a <= c:
#     print(a)
# elif c <= b <= a:
#     print(b)

# Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite random.randint(x,x) funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.

print()
######
print("_____")

a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)

print(f"a - {a}, b - {b}, c - {c}")

# if a+b>c and a+c>b and b+c>a:
#     print("Triangle is correct")
# else:
#     print("Triangle is incorrect")

## or
# longest_side = max(a, b, c)
# total_sides_sum = a + b + c
# shorts_sides_sum = total_sides_sum - longest_side
# if shorts_sides_sum > longest_side:
#     print("Triangle is correct")
# else:
#     print("Triangle is incorrect")





