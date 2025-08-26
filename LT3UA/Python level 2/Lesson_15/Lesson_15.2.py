# Уявімо, що ми маємо список предметів, і нам потрібно створити словник, де кожен предмет буде ключем, а початкове значення для кожного ключа буде встановлене як певна оцінка (наприклад, 0).

# dict_2 = dict([["table", 0], ["desk", 1], ["PC", 2]])
# print(dict_2)


# items = ["table", "desk", "pc"]
# keys = [0, 1, 2]
#
# dictionary = dict(zip(items, keys))
# print(dictionary)


items = ["table", "desk", "pc"]
default_value = 0
my_dict = dict.fromkeys(items, default_value)
print(my_dict)
