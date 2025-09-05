##Order and discounts app

subtotal = float(input("What is total sum of your order ?"))
member = input("Are you a member ? yes/no").lower()

is_member = False
if member == "yes":
    is_member = True

if subtotal < 100:
    shipping_cost = 10
else:
    shipping_cost = 0

if subtotal >= 50:
    discount = 5
else:
    discount = 0

if is_member:
    member_discount = 10
else:
    member_discount = 0

print("Order price: ", subtotal)
print("Discount: ", float(discount + member_discount))
print("Shipping cost: ", float(shipping_cost))
print("-----------------")
print("Total price is: ", float(subtotal + shipping_cost - member_discount - discount))

# working app, but without shipping costs
# if subtotal < 100:
#     subtotal += 10
#
# print(f"The total price with shipping cost is {subtotal}")
#
# if subtotal >= 50:
#     subtotal -= 5
#
# print(f"The total price with shipping cost is {subtotal} (<50)")
#
# if is_member:
#     subtotal -= 10
#
# print(f"The total price with shipping cost is {subtotal} and member status")
#
