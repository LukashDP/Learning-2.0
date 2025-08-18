# Створіть програму, яка приймає список чисел зроблений за допомогою range. Виведіть кожне число, зведене в квадрат, за допомогою вкладеного циклу.

list_1 = list(range(int(input("Invite number: "))))
print(list_1)

for i in list_1:
    # print(f"{i ** 2}")
    print(pow(i, 2))