# Створіть 2 списки з декількома різними словами.Об'єднайте їх за допомогою методу списку. Виведіть кожне слово, до кожного слова вказівник на його довжину (кількість символів) у форматі: "слово (довжина)".
# Використайте цикл for для цього.

list_1 = ["Alop", "hopoi", "nipolahqy"]
list_2 = ["zbxp", "qta", "ydhd"]
list_1.extend(list_2)
print(list_1)

for words in list_1:
    print(f"Your word {words.upper()} and have {len(words)} symbols")