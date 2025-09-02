# Створіть функцію  яка просить користувача створити список чисел та розрахуйте середнє значення списку чисел  і друку результат

def summa1():
    a = input("Enter numbers: ").split()
    b = a
    print(sum(int(x) for x in b) / len(b))

summa1()