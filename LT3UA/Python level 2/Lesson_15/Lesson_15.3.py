# Напишіть програму для створення словника, де ключами будуть імена студентів, а значеннями - їхні середні бали

# ivanov = 3, 4, 5
# petrov = 6, 4, 3
# vasilev = 4, 9, 1
#
# dict_3 = ([["Ivanov", round(sum(ivanov)/len(ivanov), 2)],["Petrov", round(sum(petrov)/len(petrov), 2)], ["Vasilev", round(sum(vasilev)/len(vasilev), 2)]])
# print(dict_3)


students = {"Ivanov": [3, 4, 5],"Petrov": [6, 4, 3],"Vasilev": [4, 9, 1]}
average_points = {name: round(sum(grades) / len(grades), 2) for name, grades in students.items()}
print(average_points)