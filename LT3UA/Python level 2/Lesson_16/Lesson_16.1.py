# d = { 'name': 'John Doe',  'age': 30, 'city': 'New York', 'email': 'johndoe@example.com'}
# Попросіть користувача ввести ключ, який він бажає видалити, і видаліть цей елемент зі словника. Та виведіть на екран змінений словник.


d = { 'name': 'John Doe', 'age': 30, 'city': 'New York', 'email': 'johndoe@example.com'}
a = input("Enter key: ")
b = list(d.keys())
for c in b:
    if c == a:
        q = d.pop(c)
print(d)