# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite
# kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

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

print()
print("------")