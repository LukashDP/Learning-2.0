list_items_str = input("type 4 random words: ")
list_items = list_items_str.split(" ")
print(list_items)

list_items = list_items[:-2]
print(list_items)

new_items = input("Enter your name: ")
new_items = new_items.split()
list_items.append(new_items)
print(list_items)


# Попросіть користувача ввести рядок з 4 словами, збережіть це у список, видаліть два останні елементи. І додайте в кінець один елемент з вашим іменем.