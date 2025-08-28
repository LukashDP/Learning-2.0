# d = {'name': 'Alice Smith', 'age': 25, 'city': 'Los Angeles', 'email': 'alice.smith@example.com', 'favorite_subjects': ['Mathematics', 'History', 'Literature']} Виведіть з цього словника значення 'favorite_subjects' використовуючи цикл.

d = {'name': 'Alice Smith', 'age': 25, 'city': 'Los Angeles', 'email': 'alice.smith@example.com', 'favorite_subjects': ['Mathematics', 'History', 'Literature']}
a = 'favorite_subjects'
b = list(d.keys())
for c in b:
    if c == a:
        print(d.get(c))