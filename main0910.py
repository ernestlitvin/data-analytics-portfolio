##
import random
import string

q_length = int(input("Enter the length of password:"))
q_digits = int(input("How many digits should be in the password?"))
q_symbols = int(input("How many symbols should be in the password?"))
letters_length = 0

if q_digits + q_symbols > q_length:
    print("The sum of digits and symbols are bigger than the length of password")
else:
    letters_length = q_length - q_digits - q_symbols
    print(f"Length of letters in password - {letters_length}")

    r_digits = ""
    for i in range(q_digits):
        r_digits += random.choice(string.digits)

    # r_digits = "".join(random.choice(string.digits) for x in range(q_digits)) ## best alternative way

    print(f"Random digits in password - {r_digits}")

    r_symbols = "".join(random.choice(string.punctuation) for x in range(q_symbols))
    print(f"Random symbols in password - {r_symbols}")

    r_letters = "".join(random.choice(string.ascii_letters) for x in range(letters_length))
    print(f"Random letters in password - {r_letters}")

    full_psw = r_digits + r_symbols + r_letters
    print(f"Full password - {full_psw}")

    final_psw = "".join(random.sample(full_psw, k=q_length))
    print(f"Final shuffled password - {final_psw}")
