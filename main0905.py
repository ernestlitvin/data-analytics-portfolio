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


numbers = [-12, -5, 1, 505, 1403, 22042, 1235334]
for number in numbers:
    if number > 0 and number % 2 == 0:
        print(f"The needed number was found {number}.")

numbers = [2, 5, 14, 54]
total_sum = 0
for number in numbers:
    total_sum += number
print(total_sum)