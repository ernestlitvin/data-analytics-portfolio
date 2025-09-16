import random


def function_with_print(a, b):
    print(a + b) # Просто показывает результат

def function_with_return(a, b):
    return a + b # Возвращает результат для дальнейшего использования

result1 = function_with_print(5, 10) # На экране напечатается 15
# Но в переменной result1 теперь лежит None (ничего)

result2 = function_with_return(5, 10) # На экране ничего не напечатается
# Но в переменной result2 теперь лежит число 15
print(result2 * 2) # Мы можем использовать результат. Выведет 30.

def print_list_items(items):
    for item in items:
        print(item)

my_plants = ["Роза", "Тюльпан"]
print_list_items(my_plants) # Передаем список в функцию

# Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.
print()
print("-----")

def sum_and_print(a, b):
    result = a + b
    print(result)
sum_and_print(5, 10)

# alternative way
# def suma(a, b):
#     return a + b
# print(suma(10,20))

## additionally like an example
# result = suma(10, 20)
# final_result = result * 2
# print(final_result) # Выведет 60

# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
print()
print("-----")

def PISq():
    return 9.8596
print(PISq())

# Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
print()
print("-----")

def multipl(a,b):
    return a * b
print(multipl(5,6))
##
# result = multipl(5,6)
# print(result)

# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
print()
print("-----")
def print_items_list(items):
    for item in items:
        print(item, end=" ")
my_plants = ["azuolas", "pusis", "berzas", "egle", "liepa", "klevas", "saulegraza", "ramune", "roze", "tulpe"]
print_items_list(my_plants)

# Sukurkite Funkciją kuri priima du kintamuosius, min ir max reikšmėms nustatyti ir
# sugeneruoja random int skaičių ir jį gražintų.
print()
print("-----")

def get_rnd_num(min_val,max_val):
    return random.randint(min_val,max_val)
random_num = get_rnd_num(1,10)
print(random_num)

print()
print("-----")
# Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų.
# Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.

def generate_random_list(min_val, max_val, length):
    random_list = []
    for i in range(length):
        num = random.randint(min_val,max_val)
        random_list.append(num)
    return random_list

li = generate_random_list(1,10,5)
print(li)

print()
print("-----")
# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.

def sum_generated_list(li):
    return sum(li)
suma = sum_generated_list(li)
print(suma)

# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.
print()
print("-----")
def avg_generated_list(li):
    return sum(li) / len(li)
avg = avg_generated_list(li)
print(avg)

# Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.
print()
print("-----")

def draw_rectangle(height,width):
    for row in range(height):
        for col in range(width):
            print("* ", end=" ")
        print()
draw_rectangle(5,10)

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
print()
print("-----")

# sent = "Šiandien labai graži diena"
# print(sent)
# length = len(sent)
# print(f"The amount of all symbols in a string - {length}")
# space_count = sent.count(" ")
# print(f"The amount of spaces in a string - {space_count}")
# symbols = len(sent) - space_count
# print(f"The amount of symbols in a string - {symbols}")

def symbols_spaces_count(sentence):
    symbols_count = 0
    spaces_count = 0
    for char in sentence:
        if char == " ":
            spaces_count += 1
        else:
            symbols_count += 1
    return symbols_count, spaces_count

s_count, sp_count = symbols_spaces_count("Jeigu jus norite gauti pinigu, tai reiketu juos uzdirbti")
print(f"Symbols count: {s_count}")
print(f"Spaces count: {sp_count}")

# alternative way
# def symb(sentence):
#     space_count = sentence.count(" ")
#     symbols = len(sentence) - space_count
#     return symbols, space_count
#
# symbol_count, space_count = symb("Šiandien labai graži diena")
# print(f"Amount of symbols: {symbol_count}")
# print(f"Amount of spces: {space_count}")

# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų.
# Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.
print()
print("-----")

def rev_sent(sentence):
    reversed_str = ""
    for char in reversed(sentence):
        reversed_str += char
    return reversed_str

ex = rev_sent("Ka daryti")
print(ex)

## alternative way
# def reversed_sentence(sentence):
#     return sentence[::-1]
# ex = reversed_sentence("Šiandien labai graži diena")
# print(ex)

# Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabal satyr” ir atspausdina rezultatą
print()
print("-----")

def rev_words(sentence):
    sentence = sentence.split()
    reversed_words = ""
    for word in sentence:
        reversed_words += word[::-1] + " "
    return reversed_words

he = rev_words("Nu ziurek kaip ten buna, o pinigu nera")
print(he)

## alternative way
# def rev_words_short(sentence):
#     words = sentence.split()
#     reversed_words_list = [word[::-1] for word in words]
#     return " ".join(reversed_words_list)
#
# he = rev_words_short("Nu ziurek kaip ten buna, o pinigu nera")
# print(he)

