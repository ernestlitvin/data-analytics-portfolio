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

#alternative way with for
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

# Naudokite funkcija random.randint(x,x). Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10.
# Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose [], 0 -  (), didesni už 0 {}.   [-4],  (0)
print("-------------")
print()
print()
x = random.randint(-10,10)
y = random.randint(-10,10)
z = random.randint(-10,10)
print(x, y, z)

if -10 <= x < 0:
    print(f"[{x}]")
elif 0 < x <= 10:
    print(f"{{{x}}}")
else:
    print(f"({x})")

if -10 <= y < 0:
    print(f"[{y}]")
elif 0 < y <= 10:
    print(f"{{{y}}}")
else:
    print(f"({y})")

if -10 <= z < 0:
    print(f"[{z}]")
elif 0 < z <= 10:
    print(f"{{z}}")
else:
    print(f"({z})")

## alternative way with for

# numbers = [x,y,z]
# for num in numbers:
#     if -10 <= num < 0:
#         print(f"[{num}]")
#     elif 0 < num <= 10:
#         print(f"{{{num}}}")
#     else:
#         print(f"({num})")

# Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų- 4 % nuolaida.
# Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama.
# Žvakių kiekį generuokite random.randint(x,x) funkcija nuo 5 iki 3000.
print("-------------")
print()
print()

x = random.randint(5,3000)
print(x)
candle_price = 1
sum_can = 0

if x > 2000:
    sum_can = (x * candle_price * 0.96)
elif x > 1000:
    sum_can = (x * candle_price * 0.97)
else:
    sum_can = x * candle_price
print(f"Candle amount - {x}. Total price of candles - {round(sum_can,2)} EUR")
print("-------------")
print()
print()

# Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100.
# Paskaičiuokite jų aritmetinį vidurkį. Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10 arba didesnės nei 90.
# Abu vidurkius atspausdinkite. Rezultatus apvalinkite iki sveiko skaičiaus.

x = random.randint(0,100)
y = random.randint(0,100)
z = random.randint(0,100)

print(x, y, z)

filtered_sum = 0
filtered_count = 0

if x > 10 and x < 90:
    filtered_sum += x
    filtered_count += 1
if y > 10 and y < 90:
    filtered_sum += y
    filtered_count += 1
if z > 10 and z < 90:
    filtered_sum += z
    filtered_count += 1

print(f"Filtered sum - {filtered_sum}")
print(f"Filtered count - {filtered_count}")

print(f"Average_1 is - {round((x + y + z) / 3,0)}")
if filtered_count == 0:
    print(f"Average_2 not available - No numbers")
else:
    print(f"Average_2 is - {round(filtered_sum / filtered_count,0)}")

print("-------------")
print()
print()
# Padarykite skaitmeninį laikrodį, rodantį valandas, minutes ir sekundes.
# Valandom, minutėm ir sekundėm sugeneruoti panaudokite funkciją random.randint(x,x).
# Sugeneruokite skaičių nuo 0 iki 300. Tai papildomos sekundės. Skaičių pridėkite prie jau sugeneruoto laiko.
# Atspausdinkite laikrodį prieš ir po sekundžių pridėjimo ir pridedamų sekundžių skaičių.

sec = random.randint(0,59)
min = random.randint(0,59)
hour = random.randint(0,23)
add = random.randint(0,300)
print(hour,min,sec)

print(f"Random time is {hour}:{min}:{sec}")

min_to_sec = min * 60
hour_to_min_to_sec = hour * 60 * 60
all_sec = sec + min_to_sec + hour_to_min_to_sec

print(f"Random time convereted to seconds - {all_sec} ")
print("------")
print(f"Additional seconds - {add}")
rnd_time_and_add_secs = all_sec + add
print(f"Randome time seconds + additional time - {rnd_time_and_add_secs}")
print("------")

back_time_hours = rnd_time_and_add_secs // 3600
print(f"New hour(s) - {back_time_hours}")

seconds_left_new = rnd_time_and_add_secs % 3600
print(f"New all seconds left - {seconds_left_new}")

print("------")
back_time_minutes = seconds_left_new // 60
print(f"New minute(s) - {back_time_minutes}")
back_time_seconds = seconds_left_new % 60
print(f"New second(s) - {back_time_seconds}")

print("------")
print(f"New random time is - {back_time_hours}:{back_time_minutes}:{back_time_seconds}")

if back_time_hours < 10:
    hours_str = f"0{back_time_hours}"
else:
    hours_str = str(back_time_hours)

if back_time_minutes < 10:
    minutes_str = f"0{back_time_minutes}"
else:
    minutes_str = str(back_time_minutes)

if back_time_seconds < 10:
    seconds_str = f"0{back_time_seconds}"
else:
    seconds_str = str(back_time_seconds)

final_time = f"{hours_str}:{minutes_str}:{seconds_str}"
print(f"New formatted time - {final_time}")

print("%02d:%02d:%02d" % (back_time_hours,back_time_minutes,back_time_seconds)) ## -> alternative way
print(f"{back_time_hours:02d}:{back_time_minutes:02d}:{back_time_seconds:02d}") ## -> best formatted way



