temperature_outside = int(input("How temperature outside? "))
temperature_comfort = int(input("How temperature comfort for you? "))
if temperature_outside > temperature_comfort:
    print("Turn on conditioner")
else:
    print("You might be comfortable without air conditioning")

# Напишіть програму, яка порівнює дві змінні: temperature_outside та temperature_comfort. Якщо temperature_outside вище temperature_comfort, виведіть "Увімкніть кондиціонер". Якщо нижче, виведіть "Можливо, вам буде комфортно без кондиціонера".