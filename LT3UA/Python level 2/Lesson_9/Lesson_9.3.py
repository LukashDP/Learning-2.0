# Напишіть програму, яка приймає від користувача довжину сторін прямокутника та обчислює його периметр і площу. Виведіть результат у такому форматі:
# Довжина: [довжина сторони]
# Ширина: [ширина сторони]
# Периметр: [значення периметра]
# Площа: [значення площі]

length_rectangle = int(input("Input length of rectangle: "))
width_rectangle = int(input("Input width of rectangle: "))
perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
area_rectangle = length_rectangle * width_rectangle
print(f"Length: {length_rectangle} \nWidth: {width_rectangle} \nPerimeter: {perimeter_rectangle} \nArea: {area_rectangle}")