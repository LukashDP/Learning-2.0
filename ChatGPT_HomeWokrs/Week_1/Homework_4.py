# l = [1, 2, 2, 3, 4, 4]
# print(list(set(l)))

l = [6, 5, 1, 2, 2, 3, 4, 4]
unique = []
for item in l:
    if item not in unique:
        unique.append(item)
print(unique)