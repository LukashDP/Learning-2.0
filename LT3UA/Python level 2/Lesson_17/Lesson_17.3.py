# Напишіть програму, яка приймає масу тіла і його швидкість, та визначає його кінетичну енергію. Потім виведіть повідомлення про ступінь руху об'єкта (спокій, повільний рух, швидкий рух) за допомогою умовної конструкції. (Розрахунок кінетичної енергії за формулою E_kin = 0.5 * m * (v**2))

m = int(input("Enter massa object: "))
v = int(input("Enter velocity object: "))
e_kin = 0.5 * m * (v ** 2)

if e_kin <= 10:
    print("Degree of motion of an object >> calm movement")
elif e_kin <= 50:
    print("Degree of motion of an object >> slow movement")
else:
    print("Degree of motion of an object >> fast movement")