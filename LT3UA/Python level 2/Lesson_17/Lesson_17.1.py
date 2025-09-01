# Напишіть програму, яка запитує у користувача суму в одній валюті (наприклад, долари) та конвертує її в іншу валюту (наприклад, євро), використовуючи поточний курс обміну. Якщо користувач вибирає USD, конвертувати в EUR; якщо вибирає EUR, конвертувати в USD.
from locale import currency

currency = input("Select currency EUR/USD: ")
summa = int(input("Enter summa: "))
usd = 40
eur = 45
if currency == "eur":
    print(usd * summa)
elif currency == "usd":
    print(eur * summa)
else:
    print("Enter correct currency")
