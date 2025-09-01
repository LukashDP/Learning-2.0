# Напишіть програму, яка приймає температуру в градусах Цельсія і виводить повідомлення про стан води (рідка, тверда, газоподібна) в залежності від введеної температури.

temperature_water = int(input("Enter temperature water: "))
if temperature_water < 0:
    print("ice water")
elif temperature_water <= 100:
    print("liquid water")
else:
    print("vaporous water")