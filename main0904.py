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

item_name = "Banana"
quantity = 5
price = 7.45

total_price = quantity * price

print("Receipt: ")
print("Item: ", item_name)
print("Quantity: ", quantity)
print("Total price: ", total_price)
print()

# name = input("What is your name? ")
# color = input("What is your favourite color")
# print(f"Hello {name}! Your favourite color is {color}")
# print()
#
# a = input("Please enter the width of the square ")
# a_int = int(a)
# b = input("Please enter the height of the square ")
# b_int = int(b)
# a_b = a_int*b_int
# print(f"The area of square is {a_b}  ")

# subjects = ["math", "history", "pe", "geography", "english language"]
# second_item = subjects[1]
# print(second_item)
# subjects.append("lithuanian language")
# subjects.insert(0,"german language")
# print(subjects)
# print(len(subjects))

# num = random.randint(-5,5)
# print(num)
# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")
#
# is_logged_in = True
# is_admin = True
# if is_logged_in and is_admin:
#     print("Hello admin")
# else:
#     print("Hello user")
#
# psw = input("What is the password ?")
# # psw = random.randint(1, 3)
# # print(psw)
# if psw == "12345":
#     print("Password is correct")
# else:
#     print("Password is incorrect")

# rating = int(input("Please tell your rating: "))
# mot = input ("Do you have motivation letter ?")
# orating = int(input ("What is your outside rating ?"))
#
# if (rating >= 85) and (mot == "Yes" or orating >= 7):
#         print("Accepted")
# else:
#     print("Rejected")

### alternative way
# rating = int(input("Please tell your rating: "))
# mot_answer = input("Do you have motivation letter? (yes/no) ")
# orating = int(input("What is your outside rating? "))
#
    # has_motivation_letter = False
    # if mot_answer.lower() == "yes":
    #     has_motivation_letter = True
    #
    # or even: if mot_answer.lower() == "yes":
#     has_motivation_letter = True
# else:
#     has_motivation_letter = False

# if rating >= 85 and (has_motivation_letter or orating > 7):
#     print("Accepted")
# else:
#     print("Rejected")

print()
##ATM##

# balance = int(1000)
#
# print(f"Your balance is {balance}")
# action = input("What action do you want to do: deposit/withdraw/balance ? ")
#
# if action == "deposit":
#     deposit_amount = int(input("How much do you want to deposit: "))
#     balance = balance + deposit_amount
#     print(f"Action done. Your balance is {balance} ")
# elif action == "withdraw":
#     withdraw_amount = int(input("How much do you want to withdraw: "))
#     if withdraw_amount > balance:
#         print("You don't have enough money")
#     elif withdraw_amount < 0:
#         print("Wrong amount")
#     else:
#         balance = balance - withdraw_amount
#         print(f"Action done. Your balance is {balance}")
# elif action == "balance":
#     print(balance)
# else:
#     print("Invalid action")