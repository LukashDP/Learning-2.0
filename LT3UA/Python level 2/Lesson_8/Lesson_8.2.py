# Створіть програму, яка приймає рядок від користувача та заміняє всі входження символу 'a' на '*', якщо символ ‘а’ відсутній до відповідне повідомлення.


user_print2 = input("Input test: ")
empty = user_print2.find("a")
if empty == -1:
    print("Your text don't have symbol a")
else:
    print(user_print2.replace("a", "*"))
