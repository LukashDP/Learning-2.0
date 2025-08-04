price = float(input("How much does it cost: "))
discount = float(input("Which discount do you have?: "))
your_discount = (price // 100 * discount)
final_price = price - your_discount

print("Your discount = ", your_discount)
print("Final price = ", final_price )