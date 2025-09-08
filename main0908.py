## Sukurkite keturis kintamuosius ir random.randint(x,x) funkcija sugeneruokite jiems reikšmes nuo 0 iki 2.
# Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).
import random

a = random.randint(0,2)
b = random.randint(0,2)
c = random.randint(0,2)
d = random.randint(0,2)
print(a, b, c, d)

zeros = 0
ones = 0
twos = 0

if a == 0:
    zeros += 1
elif a == 1:
    ones += 1
elif a == 2:
    twos += 1

if b == 0:
    zeros += 1
elif b == 1:
    ones += 1
elif b == 2:
    twos += 1

if c == 0:
    zeros += 1
elif c == 1:
    ones += 1
elif c == 2:
    twos += 1

if d == 0:
    zeros += 1
elif d == 1:
    ones += 1
elif d == 2:
    twos += 1

print(f"Zeros count - {zeros}, Ones count - {ones}, Twos count - {twos}")

#alternative way with massive
# numbers = []
# a = random.randint(0,2)
# numbers.append(a)
# b = random.randint(0,2)
# numbers.append(b)
# c = random.randint(0,2)
# numbers.append(c)
# d = random.randint(0,2)
# numbers.append(d)
# print(numbers)
# count_numbers_0 = numbers.count(0)
# count_numbers_1 = numbers.count(1)
# count_numbers_2 = numbers.count(2)
# print(f"Zeros count {count_numbers_0}. Ones count {count_numbers_1}. Twos count {count_numbers_2}")


#alternative way with cycle
# a = random.randint(0,2)
# b = random.randint(0,2)
# c = random.randint(0,2)
# d = random.randint(0,2)
# print(a, b, c, d)
# numbers = [a,b,c,d]
# zeros, ones, twos = 0,0,0
#
# for num in numbers:
#     if num == 0:
#         zeros += 1
#     elif num == 1:
#         ones += 1
#     else:
#         twos += 1
# print(f"Zero_count {zeros}, Ones_count {ones}, Twos_count {twos}")





