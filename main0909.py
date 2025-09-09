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

# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus (Jonas Jonaitis).
# Atspausdinti trumpesnį stringą.
print()
print("_____")
name = "Daniel"
surname = "Radcliffe"

shortest = min(name,surname,key=len)
print(shortest)

# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Vardą atspausdinti tik didžiosiom raidėm, o pavardę tik mažosioms. (LEONARDO dicaprio)
name = "Daniel"
surname = "Radcliffe"
print(name.upper(),surname.lower())

# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš pirmų vardo ir pavardės kintamųjų reikšmių raidžių.
# Jį atspausdinti.

name = "Daniel"
surname = "Radcliffe"
letters = name[0] + surname[0]
print(letters)

# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo ir pavardės kintamųjų raidžių.
# Jį atspausdinti.

name = "Daniel"
surname = "Radcliffe"
letters = name[-3:] + surname[-3:]
print(letters)

# Sukurti kintamąjį su stringu: "An American in Paris".
# Jame vis`as “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.
sent = "An American in Paris"
new_sent = sent.replace("a","A")
new_sent2 = new_sent.replace("A","*")
print(new_sent)
print(new_sent2)

new_sent = sent.replace('a', '*').replace('A', '*') ## alternative way


# Sukurti kintamąjį su stringu: "An American in Paris".
# Jame ištrinti visas balses.
# Rezultatą atspausdinti.
# Kodą pakartoti su stringais: "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".

sent1 = "An American in Paris"
sent = sent1.lower()
new_sent1 = sent.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(new_sent1)

sent2 = "Breakfast at Tiffany's"
sent = sent2.lower()
new_sent2 = sent.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(new_sent2)
