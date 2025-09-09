# Naudokite funkcija random.randint(x,x). Sugeneruokite 6 kintamuosius su atsitiktinem reikšmėm nuo 1000 iki 9999.
# Atspausdinkite reikšmes viename stringe, išrūšiuotas nuo didžiausios iki mažiausios, atskirtas tarpais.

import random

a = random.randint(1000,9999)
b = random.randint(1000,9999)
c = random.randint(1000,9999)
d = random.randint(1000,9999)
e = random.randint(1000,9999)
f = random.randint(1000,9999)
print(a,b,c,d,e,f)

mas = [a,b,c,d,e,f]
mas.sort(reverse=True)
print(mas)

for number in mas:
    print(number, end=" ")




