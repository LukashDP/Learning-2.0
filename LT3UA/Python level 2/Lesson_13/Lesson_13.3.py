# Стас і Маша вирішили скористатися послугою «Оплата частинами» для придбання комп'ютера. Вони знають загальну вартість комп'ютера (45999 грн) та розмір місячного платежу (7500 грн). Ваше завдання - допомогти їм визначити, скільки місяців їм потрібно буде платити, щоб повністю розрахуватися за комп'ютер.
# Виведіть це число користувачу для його зручності та кращого розуміння умови оплати.

# total_price_pc = 45999
# price_each_mounth = 7500
# number_months = total_price_pc // price_each_mounth + 1
# print(f"Total number of months to pay {number_months} ")


total_price_pc = 45999
price_each_mounth = 7500
number_months = (total_price_pc + price_each_mounth - 1) // price_each_mounth
print(f"Total number of months to pay {number_months} ")