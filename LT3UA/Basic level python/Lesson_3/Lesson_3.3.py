first_password = input("Input first password: ")
second_password = input("Enter password again: ")
assert first_password == second_password, "passwords do not match "

print("Password match")

# Користувач повинен ввести пароль двічі для підтвердження. Необхідно перевірити, чи обидва введені паролі співпадають. Якщо паролі співпадають, вивести повідомлення 'пароль вірний' . Якщо паролі не співпадають, користувач отримує помилку.